import sys
from src.prediction.logger import logging
from src.prediction.exception import CustomException
from src.prediction.components.data_ingestion import DataIngestionConfig, DataIngestion

if __name__=="__main__":
    logging.info("The excecution started")

    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
    