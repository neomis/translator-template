"""Translator for .example files."""
import os
from io import StringIO
from typing import List, Dict, Any
from loguru import logger
import arrow
import pandas as pd
from translator_template.config import ENCODING, OUT_PATH
from translator_template.utils import write_json, validate_path


def main(file_path: str) -> None:
    """Process .example file."""
    logger.info("STARTING TRANSLATOR: EXAMPLE")
    validate_path(OUT_PATH, permission='w')
    with open(file_path, 'r', encoding=ENCODING) as file_handle:
        lines: List[str] = file_handle.read().strip().split('\n')
        file_handle.close()
    record: Dict[str, Any] = {}
    line_num: int = 0
    while len(lines) > 0:
        line: str = lines.pop(0).strip()
        line_num += 1
        if line.startswith('#'):
            continue
        if line == '':
            continue
        if ':' not in line:
            raise ValueError(f"Invalid line detected[{line_num}]: {line}")
        key: str = ""
        value: Any = None
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        logger.debug(f"{key}: {value}")
        if value == '':
            key_line_num = line_num
            temp_value: List[str] = []
            found_end = False
            while len(lines) > 0:
                line = lines.pop(0).strip()
                line_num += 1
                if line.upper() == 'END':
                    found_end = True
                    break
                temp_value.append(line)
            if not found_end:
                raise ValueError(
                    f"Key: {key} missing END at line {key_line_num}")
            value = pd.read_csv(StringIO("\n".join(temp_value)), sep='\t')
            logger.debug(f"\n{value}")
        if '_DATE' in key:
            value = arrow.get(value, tzinfo='local')

        record[key] = value
    file_name: str = os.path.split(file_path)[1]
    file_name = os.path.splitext(file_name)[0]
    write_json(record, os.path.join(OUT_PATH, file_name))
