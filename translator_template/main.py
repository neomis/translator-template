"""Main program."""
import os
from time import sleep
from multiprocessing import Pool
import pidfile
from loguru import logger
from translator_template import translator
from .utils import validate_file, validate_path, read_dir
from .config import (ENVIRONMENT, QUEUE_PATH, WORK_PATH, REJECT_PATH,
                     THREADS, PID_FILE, LOG_FILE, LOG_LEVEL, SLEEP_TIME)


def spool_file(file_path: str, **kwargs) -> None:
    """Process Single file."""
    try:
        base_path, file_name = os.path.split(file_path)
        logger.info(f"PROCESS FILE: {file_name}")
        for key, value in kwargs.items():
            logger.debug(f"{key}: {value}")
        validate_file(file_path, permission='w')
        validate_path(WORK_PATH)
        validate_path(REJECT_PATH)
        try:
            os.rename(file_path, os.path.join(WORK_PATH, file_name))
        except Exception as error:
            logger.debug(error)
            raise ValueError(
                f"Failed to move file: {file_name} to WORK_PATH: {WORK_PATH}") from error
        file_path = os.path.join(WORK_PATH, file_name)
        # Translate based on file extension
        file_ext = os.path.splitext(file_name)[1]
        if file_ext != '':
            file_ext = file_ext[1:]
        method_name = f"TRANSLATE_{file_ext.upper()}"
        logger.debug(f"METHOD_NAME: {method_name}")
        if not hasattr(translator, method_name):
            raise ValueError(f"No translator found for file: {file_name}")
        getattr(translator, method_name)(file_path)
        if ENVIRONMENT == "PRODUCTION":
            try:
                os.unlink(file_path)
                return
            except Exception as error:
                logger.debug(error)
                raise ValueError(
                    "Failed to remove file: {file_path}") from error
        else:
            try:
                os.rename(file_path, os.path.join(base_path, file_name))
                return
            except Exception as error:
                logger.debug(error)
                raise ValueError(
                    f"Failed to move file: {file_name} to QUEUE_PATH: {base_path}") from error
    except Exception as error:
        logger.debug(error)
        if ENVIRONMENT == "PRODUCTION":
            try:
                os.rename(file_path, os.path.join(REJECT_PATH, file_name))
            except Exception as suberror:
                logger.error(
                    f"Failed to move file: {file_name} to REJECT_PATH: {REJECT_PATH}")
                logger.debug(suberror)
                return
        else:
            try:
                os.rename(file_path, os.path.join(base_path, file_name))
            except Exception as suberror:
                logger.debug(suberror)
                raise ValueError(
                    f"Failed to move file: {file_name} to QUEUE_PATH: {base_path}") from error
            raise


def spooler(**kwargs) -> None:
    """Spool files in directory."""
    for key, value in kwargs.items():
        logger.debug(f"{key}: {value}")
    logger.debug(f"QUEUE_PATH: {QUEUE_PATH}")
    validate_path(QUEUE_PATH)
    file_list = []
    for file_name in read_dir(QUEUE_PATH):
        file_path = os.path.join(QUEUE_PATH, file_name)
        try:
            validate_file(file_path, permission='w')
            file_list.append(file_path)
        except (ValueError, TypeError) as error:
            logger.warning(error)
            continue
    if len(file_list) > 0:
        if THREADS <= 1:
            for file_path in file_list:
                spool_file(file_path)
        else:
            with Pool(THREADS) as pool:
                pool.map(spool_file, file_list)


def spool_daemon(**kwargs) -> None:
    """Run as daemon server."""
    try:
        with pidfile.PIDFile(PID_FILE):
            logger.add(LOG_FILE, level=LOG_LEVEL, rotation="100 MB")
            while True:
                try:
                    spooler(**kwargs)
                except KeyboardInterrupt as error:
                    logger.debug(error)
                    logger.info("User initialized an exit")
                    break
                except Exception as error:
                    logger.error(error)
                sleep(SLEEP_TIME)
    except pidfile.AlreadyRunningError as error:
        logger.error(error)
        raise ValueError("Already running") from error
