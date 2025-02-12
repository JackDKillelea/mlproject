import sys
import os
import numpy as np
import pandas as pd
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from exception_handler import CustomException
from logger import logging
from utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_object_file_pickle_path = os.path.join("artifact", "preprocessor.pkl")

class DataTransformer:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_transformer_object(self):
        try:
            numerical_features = ["writing score", "reading score"]
            categorical_features = [
                "gender",
                "race/ethnicity",
                "parental level of education",
                "lunch",
                "test preparation course"
            ]

            logging.info("Starting pipelines")

            numerical_pipeline = Pipeline(
                steps = [
                    # Handle missing values
                    ("imputer", SimpleImputer(strategy="median")),
                    # Do scaling
                    ("scaler", StandardScaler())
                ]
            )

            logging.info("Numerical pipeline has completed")

            categorical_pipeline = Pipeline(
                steps = [
                    # Handle missing values
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    # Turn categorical data into a one-hot numeric array
                    ("ohe", OneHotEncoder()),
                    # Do scaling
                    ("scaler", StandardScaler(with_mean=False))
                ]
            )

            logging.info(f"Numerical features: {numerical_features}")
            logging.info(f"Categorical features: {categorical_features}")

            preprocessor = ColumnTransformer(
                [
                    ("numerical_pipeline", numerical_pipeline, numerical_features),
                    ("categorical_pipeline", categorical_pipeline, categorical_features)
                ]
            )

            return preprocessor
        except Exception as e:
            raise CustomException(e, sys)
        
    def init_data_transformation(self, train_path, test_path):
        try:
            logging.info("Attempting to read training and test data")
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Attempting to get preproccessor object")
            preproccessing_obj = self.get_transformer_object()

            target_column_name ="math score"

            input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info("Applying preprocessing object on training dataframe and test dataframe")

            input_feature_train_array = preproccessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_array = preproccessing_obj.transform(input_feature_test_df)
            
            train_array = np.c_[
                input_feature_train_array, np.array(target_feature_train_df)
            ]

            test_array = np.c_[
                input_feature_test_array, np.array(target_feature_test_df)
            ]
            
            save_object(
                self.data_transformation_config.preprocessor_object_file_pickle_path,
                preproccessing_obj
            )

            return (
                train_array,
                test_array,
                self.data_transformation_config.preprocessor_object_file_pickle_path
            )
        except Exception as e:
            raise CustomException(e, sys)