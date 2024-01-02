import sys
from src.prediction.logger import logging
from src.prediction.exception import CustomException

if __name__=="__main__":
    logging.info("The excecution started")

    try:
        a= 1/0

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
    