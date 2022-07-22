# Translator Template

Basic Python template for creating a file translation spooler.

## How to Install

```bash
python3 -m venv /opt/translator_template
source /opt/translator_template/bin/activate
pip install --upgrade pip setuptools wheel
pip install translator_template
```

## How to Run

Process a single file

`translate_file <file_path> [--loglevel=(DEBUG, INFO, ERROR)]`

Run the spooler once

`translate_spool [--loglevel=(DEBUG, INFO, ERROR)]`

Run the spooler as a daemon

`translate_spool -d [--loglevel=(DEBUG, INFO, ERROR)]`

## Sample ENV FILE:

```bash
## GLOBAL SETTINGS
# ENVIRONMENT = PRODUCTION
# ENCODING = UTF-8

## SPOOLER SETTINGS
# THREADS = 4
# QUEUE_PATH = ./spooler/queued
# WORK_PATH = ./spooler/processing
# REJECT_PATH = ./spooler/rejected
# OUT_PATH = ./spooler/finished

## DAEMON SETTINGS
# PID_FILE = translator_template.pid
# LOG_FILE = translator_template.log
# LOG_LEVEL = ERROR
# SLEEP_TIME = 5
```
## Import External Translators

See Translator-Template-Example for how to create external translators.
In short add the following line to setup.py in the external package:

```python
entry_points={
        'translator_template.translators': '<alias> = <package_name>.translator:main'
}
```

The modules will be imported automatically.