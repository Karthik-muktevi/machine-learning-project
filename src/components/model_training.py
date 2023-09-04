from src.constants import *
from src.config.configuration import *
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np
import os,sys
from src.utils import evaluate_models,save_obj
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from xgboost import XGBRegressor

@dataclass
class ModelTrainingConfig:
    trained_model_filepath = MODEL_FILEPATH

class ModelTrainer:
    def __init__(self):
        self.model_training_config = ModelTrainingConfig()

    def initiate_model_training(self,train_array,test_array):
        try:
            x_train,y_train,x_test,y_test = (train_array[:,:-1],train_array[:,-1],
                                             test_array[:,:-1],test_array[:,-1])
            
            models = {

                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "SVR" : SVR(),
                "XGBRegressor": XGBRegressor()
                }
            model_report:dict = evaluate_models(x_train=x_train,x_test=x_test,y_train=y_train,y_test=y_test,models=models)
            print(model_report)
            best_model_score = max(model_report.values())
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model = models[best_model_name]
            print(f"Best model is, Model_name: {best_model}, r2_score: {best_model_score}")

            logging.info(f"Best model is, Model_name: {best_model}, r2_score: {best_model_score}")

            save_obj(file_path=self.model_training_config.trained_model_filepath,
                     obj=best_model)



        
        
        
        
        
        except Exception as e:
            raise CustomException(e,sys)