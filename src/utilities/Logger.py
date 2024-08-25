import logging
from datetime import datetime
from config import DEBUG_MODE, IS_LOGGING_ENABLED, LOGFILE_PATH, WRITE_LOG_IN_STDOUT


class Logger:
    def __init__(self):
        if IS_LOGGING_ENABLED:
            self.logger = logging.getLogger()
            self.logger.handlers = []
            self.logger.setLevel(logging.INFO)
            logging.getLogger("telethon").setLevel(level=logging.CRITICAL)
            if WRITE_LOG_IN_STDOUT:
                # Add a StreamHandler to write logs to stdout
                stream_handler = logging.StreamHandler()
                stream_handler.setFormatter(
                    logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
                )
                self.logger.addHandler(stream_handler)
            else:
                # Add a StreamHandler to write logs in stdout
                current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
                log_name = f"{LOGFILE_PATH}/{current_datetime}.log"
                file_handler = logging.FileHandler(log_name, mode="a")
                file_handler.setFormatter(
                    logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
                )
                self.logger.addHandler(file_handler)

    def info(self, msg, write_only_in_debug_mode=False):
        if (
            write_only_in_debug_mode == True and DEBUG_MODE == False
        ) or IS_LOGGING_ENABLED == False:
            return
        self.logger.info(msg)

    def warning(self, msg, write_only_in_debug_mode=False):
        if (
            write_only_in_debug_mode == True and DEBUG_MODE == False
        ) or IS_LOGGING_ENABLED == False:
            return
        self.logger.warning(msg)

    def error(self, msg, write_only_in_debug_mode=False):
        if (
            write_only_in_debug_mode == True and DEBUG_MODE == False
        ) or IS_LOGGING_ENABLED == False:
            return
        self.logger.error(msg)


logger = Logger()
