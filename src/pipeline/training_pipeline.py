import os,sys
from src.constants import *
from src.config.configuration import *
from src.logger import logging
from src.exception import CustomException
from src.components.data_transformation import DataTransformation, DataTransformationConfig
from src.components.model_training import ModelTrainer
from src.components.data_ingestion import DataIngestion

class Train:
    def __init__(self):
        self.c = 0
        print(f"**********{self.c}****************")

    def main(self):
        obj = DataIngestion()
        train_data_path,test_data_path = obj.initiate_data_ingestion()
        data_transformation = DataTransformation()
        train_arr,test_arr,_ = data_transformation.inititate_data_transformation(train_data_path,test_data_path)
        model_trainer = ModelTrainer()
        print(model_trainer.initiate_model_training(train_array=train_arr,test_array=test_arr))
