import os, sys
import pandas as pd
from src.prediction.logger import logging
from src.prediction.exception import CustomException
from dotenv import load_dotenv
import pymysql

load_dotenv()

host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
db = os.getenv('db')

def read_sql_data():
    try:
        logging.info("Checking SQL connection")

        mydb = pymysql.connect(
            host = host,
            user = user,
            password = password,
            db = db,
            port = 3307
        )

        df = pd.read_sql_query('SELECT * FROM students', mydb)
        print(df.head())

        logging.info('Connection with SQL established')

        return df

    except Exception as e:
        raise CustomException(e,sys)