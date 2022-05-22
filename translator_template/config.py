"""Environment Config."""
import os
# GLOBAL SETTINGS
ENVIRONMENT: str = os.getenv("ENVIRONMENT", "PRODUCTION")
ENCODING: str = os.getenv("ENCODING", 'utf-8')

# SPOOLER SETTINGS
THREADS = int(os.getenv("THREADS", "4"))
QUEUE_PATH = os.getenv("QUEUE_PATH", 'spooler/queued')
WORK_PATH = os.getenv("WORK_PATH", 'spooler/processing')
REJECT_PATH = os.getenv("REJECT_PATH", 'spooler/rejected')
OUT_PATH = os.getenv("OUT_PATH", 'spooler/finished')

# DAEMON SETTINGS
PID_FILE = os.getenv("PID_FILE", "translator_template.pid")
LOG_FILE = os.getenv("LOG_FILE", "translator_template.log")
LOG_LEVEL = os.getenv("LOG_LEVEL", "ERROR")
SLEEP_TIME = int(os.getenv("SLEEP_TIME", "5"))
