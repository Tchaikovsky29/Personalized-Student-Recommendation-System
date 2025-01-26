import os
import logging

#Create a logging function that logs the information of steps and errors with proper time format and log level
def logger(file_name:str):
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    # logging configuration
    logger = logging.getLogger(file_name)
    logger.setLevel('DEBUG')

    console_handler = logging.StreamHandler()
    console_handler.setLevel('DEBUG')

    log_file_path = os.path.join(log_dir, file_name + '.log')
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel('DEBUG')

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger