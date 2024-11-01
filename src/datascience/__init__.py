import os
import sys
import logging

# to create a loggging directory


logging_str = "[%(asctime)s - %(levelname)s - %(module)s - %(message)s]"


log_dir  = "logs"

log_filepath = os.path.join(log_dir, "logging.log")

# creating a loggging directory,dont create if it already exists
os.makedirs(log_dir, exist_ok=True)

# when running the code on command line, the logs are saved in the logs directory file path ,with level , asctime
logging.basicConfig(level=logging.INFO, format=logging_str, handlers=[logging.FileHandler(log_filepath), 
                                                                      logging.StreamHandler(sys.stdout)])

logger = logging.getLogger("datasciencelogger")