# Translator Template

Basic Python template for creating a file translation spooler.

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
