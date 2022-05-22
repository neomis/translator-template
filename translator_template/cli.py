"""Click interface."""
import sys
import click
from loguru import logger
from .config import ENVIRONMENT


logger.enable(__package__)
logger.remove(0)


@click.command()
@click.argument('file_path', type=str)
@click.option('--loglevel', 'log_level', type=click.Choice(['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'], case_sensitive=False), default='ERROR')
def translate_file(file_path, log_level) -> None:
    """Translate a single file"""
    from .main import spool_file  # pylint: disable=import-outside-toplevel
    logger.add(sys.stderr, colorize=True, level=log_level)
    logger.info(f"ENVIRONMENT: {ENVIRONMENT}")
    logger.info(f"LOG LEVEL: {log_level}")
    spool_file(file_path)


@click.command()
@click.option('-d', '--daemon', 'daemon', is_flag=True, default=False, help="Run in daemon mode.")
@click.option('--loglevel', 'log_level', type=click.Choice(['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'], case_sensitive=False), default='ERROR')
def translate_spool(daemon, log_level) -> None:
    """Main Comand Line Interface"""
    from .main import spooler, spool_daemon  # pylint: disable=import-outside-toplevel
    logger.add(sys.stderr, colorize=True, level=log_level)
    logger.info(f"ENVIRONMENT: {ENVIRONMENT}")
    logger.info(f"LOG LEVEL: {log_level}")
    if daemon:
        spool_daemon()
    else:
        spooler()
