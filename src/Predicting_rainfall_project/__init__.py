import os
import sys
import logging

logging_format = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s:]"

## create a log directory
log_dir = "logs"
   #create a log file inside the "logs" directory
log_filepath = os.path.join(log_dir,"running_log.log")
os.makedirs(log_dir,exist_ok= True)


level_name = logging.INFO
logging.basicConfig(
    level= level_name, format= logging_format,
    handlers= [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
        ]
)

#create logger object
logger = logging.getLogger("Project_logger")
