import os, sys
import pandas as pd
from src.prediction.logger import logging
from src.prediction.exception import CustomException
from dataclasses import dataclass
from src.prediction.utils import read_sql_data
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    raw_file_path = os.path.join('artifacts','raw.csv')
    train_file_path = os.path.join('artifacts','train.csv')
    test_file_path = os.path.join('artifacts','test.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig

    def initiate_data_ingestion(self):
        try:
            # Reading data from sql
            logging.info("Reading data from SQL")
            df = read_sql_data()
            
            # Saving the data as raw.csv
            logging.info("Saving data as raw.csv")
            os.makedirs(os.path.dirname(self.ingestion_config.raw_file_path), exist_ok=True) 
            df.to_csv(self.ingestion_config.raw_file_path, index=False, header=True)
            
            
            # Splitting raw data into train and test split and saving

            train_set,test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_file_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_file_path, index=False, header=True)
            
            logging.info("data ingestion completed")

            return(
                self.ingestion_config.train_file_path,
                self.ingestion_config.test_file_path
            )
        except Exception as e:
            raise CustomException(e,sys)
