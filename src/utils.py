import os
import sys
import dill
from exception_handler import CustomException
from logger import logging

def save_object(file_path, object):
    try:
        logging.info("Saving Object")

        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(object, file_obj)

        logging.info("Object Saved Successfully")
    except Exception as e:
        raise CustomException(e, sys)