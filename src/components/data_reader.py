import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from exception_handler import CustomException
from logger import logging

@dataclass
class DataReaderConfig():
    raw_data_path = os.path.join("artifact", "data.csv")
    train_data_path = os.path.join("artifact", "train.csv")
    test_data_path = os.path.join("artifact", "test.csv")

class DataReader():
    def __init__(self):
        self.reader_config = DataReaderConfig()

    def initiate_data_reading(self):
        logging.info("Initiated data reading")

        try:
            df = pd.read_csv("src/notebook/data/StudentsPerformance.csv")
            logging.info("Data has been read")

            os.makedirs(os.path.dirname(self.reader_config.train_data_path), exist_ok=True)
            df.to_csv(self.reader_config.raw_data_path, index=False, header=True)

            logging.info("Train test split starting")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.reader_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.reader_config.test_data_path, index=False, header=True)

            logging.info("Completed data reading")
            
            return (self.reader_config.train_data_path, 
                self.reader_config.train_data_path)
        except Exception as e:
            raise CustomException(e, sys)
        

if __name__ == "__main__":
    obj = DataReader()
    obj.initiate_data_reading()