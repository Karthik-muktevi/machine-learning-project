import os,sys
from src.constants import *
from src.config.configuration import *
from src.logger import logging
from src.exception import CustomException
import pandas as pd
import numpy as np
import pickle
from src.utils import load_model
from sklearn.pipeline import Pipeline
import streamlit as st



class BatchPrediction:
    def __init__(self,input_file_path, 
                 model_file_path, 
                 transformer_file_path, 
                 feature_engineering_file_path):
        self.input_file_path = input_file_path
        self.model_file_path = model_file_path
        self.transformer_file_path = transformer_file_path
        self.feature_engineering_file_path = feature_engineering_file_path

    def start_batch_prediction(self):
        try:
            logging.info("Loading the saved pipeline")
            # Load the feature engineering pipeline
            
            feature_pipeline = load_model(file_path=self.feature_engineering_file_path)
            logging.info(f"Feature eng Object acessed :{self.feature_engineering_file_path}")
            # Load the data transformation pipeline
            
            preprocessor = load_model(file_path=self.transformer_file_path)

            logging.info(f"Preprocessor  Object acessed :{self.transformer_file_path}")
            
            # Load the model separately
            model =load_model(file_path=self.model_file_path)

            logging.info(f"Model File Path: {self.model_file_path}")

            # Create the feature engineering pipeline
            feature_engineering_pipeline = Pipeline([
                ('feature_engineering', feature_pipeline)
            ])
            # Read the input file
            df = pd.read_csv(self.input_file_path)


            # Apply feature engineering
            df = pd.DataFrame(feature_engineering_pipeline.transform(df))
        
            logging.info("Feature-engineereing completed.")

            # Dropping target column
            
            df=df.drop('Time_taken (min)', axis=1)
          
            logging.info(f"Columns before transformation: {', '.join(f'{col}: {df[col].dtype}' for col in df.columns)}")
            # Transform the feature-engineered data using the preprocessor
            transformed_data = preprocessor.transform(df)
            logging.info(f"Transformed Data Shape: {transformed_data.shape}")
            
            logging.info(f"Loaded numpy from batch prediciton :{transformed_data}")
            
            logging.info(f"Model Data Type : {type(model)}")
            
            predictions = model.predict(transformed_data)
            logging.info(f"Predictions done :{predictions}")

            # Create a DataFrame from the predictions array
            df_predictions = pd.DataFrame(predictions, columns=['prediction'])
            
            # Save the predictions to a CSV file
              # Specify the desired path for saving the CSV file
            df_predictions.to_csv("predictions.csv", index=False)
            logging.info(f"Batch predictions saved .")
            return st.write(predictions)

        except Exception as e:
            CustomException(e,sys)