import logging
import os
from datetime import datetime

LOG_DIR = 'logs'
LOG_DIR = os.path.join(os.getcwd(),LOG_DIR)

os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE_NAME = f"log_{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"

log_file_path = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(filename=log_file_path,
                    filemode="w",
                    format= '[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
                    level= logging.INFO)


