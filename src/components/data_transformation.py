from src.constants import *
from src.logger import logging
from src.exception import CustomException
import os, sys
from src.config.configuration import *
from dataclasses import dataclass
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder,OneHotEncoder
from sklearn.pipeline import Pipeline
from src.utils import save_obj
from src.config.configuration import PREPROCESSING_OBJ_FILEPATH,TRANSFORM_TRAIN_FILEPATH,TRANSFORM_TEST_FILEPATH,FE_OBJ_FILEPATH


class FE(BaseEstimator, TransformerMixin): 
    def __init__(self):
        logging.info("******************Feature Engineering started******************")

    def distance(self,df,lat1, lon1, lat2, lon2):
        p = np.pi/180
        a = 0.5 - np.cos((df[lat2]-df[lat1])*p)/2 + np.cos(df[lat1]*p) * np.cos(df[lat2]*p) * (1-np.cos((df[lon2]-df[lon1])*p))/2
        df['distance'] = 12734 * np.arccos(a)

    
    
    def transform_data(self,df):
        try:
            df.drop(['ID'],axis=1,inplace=True)
            self.distance(df, 'Restaurant_latitude',
                                'Restaurant_longitude',
                                'Delivery_location_latitude',
                                'Delivery_location_longitude')
            
            df.drop(['Delivery_person_ID', 'Restaurant_latitude','Restaurant_longitude',
                                'Delivery_location_latitude',
                                'Delivery_location_longitude',
                                'Order_Date','Time_Orderd','Time_Order_picked'], axis=1,inplace=True)
            
            logging.info("droping columns from our original dataset")
            
            return df
        except Exception as e:
            raise CustomException(e,sys)
        
    def fit(self,X,y=None):
        return self
        
    def transform(self,X:pd.DataFrame,y=None):
        try:    
            transformed_df=self.transform_data(X)
                
            return transformed_df
        except Exception as e:
            raise CustomException(e,sys)
        
@dataclass
class DataTransformationConfig():
    processed_obj_filepath = PREPROCESSING_OBJ_FILEPATH
    transform_train_path = TRANSFORM_TRAIN_FILEPATH
    transform_test_path = TRANSFORM_TEST_FILEPATH
    fe_obj_path = FE_OBJ_FILEPATH

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation_obj(self):
        try:
            Road_traffic_density = ['Low', 'Medium', 'High', 'Jam']
            Weather_conditions = ['Sunny', 'Cloudy', 'Fog', 'Sandstorms', 'Windy', 'Stormy']

            categorical_columns = ['Type_of_order','Type_of_vehicle','Festival','City']
            ordinal_encoder = ['Road_traffic_density', 'Weather_conditions']
            numerical_columns=['Delivery_person_Age','Delivery_person_Ratings','Vehicle_condition',
                              'multiple_deliveries','distance']

            # Numerical pipeline
            numerical_pipeline = Pipeline(steps = [
                ('impute', SimpleImputer(strategy = 'constant', fill_value=0)),
                ('scaler', StandardScaler(with_mean=False))
            ])

            # Categorical Pipeline
            categorical_pipeline = Pipeline(steps = [
                ('impute', SimpleImputer(strategy = 'most_frequent')),
                ('onehot', OneHotEncoder(handle_unknown = 'ignore')),
                ('scaler', StandardScaler(with_mean=False))
            ])

            # ordinal Pipeline
            ordinal_pipeline = Pipeline(steps = [
                ('impute', SimpleImputer(strategy = 'most_frequent')),
                ('ordinal', OrdinalEncoder(categories=[Road_traffic_density,Weather_conditions])),
                ('scaler', StandardScaler(with_mean=False))
            ])
            
            preprocessor = ColumnTransformer([
                ('numerical_pipeline', numerical_pipeline,numerical_columns ),
                ('categorical_pipeline', categorical_pipeline,categorical_columns ),
                ('ordinal_pipeline', ordinal_pipeline,ordinal_encoder )
            ])

            logging.info("Pipeline Steps Completed")
            return preprocessor

        except Exception as e:
            raise CustomException( e,sys)
        
    def get_fe_obj(self):
        try:
            feature_engineering = Pipeline(steps=[('fe',FE())])
            return feature_engineering
        except Exception as e:
            raise CustomException( e,sys)
        
    def inititate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info('Obtaining FE object')
            fe_obj = self.get_fe_obj()
            train_df = fe_obj.fit_transform(train_df)
            test_df = fe_obj.transform(test_df)
            train_df.to_csv("train_data.csv")
            test_df.to_csv("test_data.csv")

            preprocessing_obj = self.get_data_transformation_obj()
            target_column = "Time_taken (min)"
            X_train = train_df.drop(columns = target_column, axis = 1)
            y_train = train_df[target_column]

            X_test = test_df.drop(columns = target_column, axis = 1)
            y_test = test_df[target_column]

            X_train = preprocessing_obj.fit_transform(X_train)
            X_test = preprocessing_obj.transform(X_test)
            train_arr = np.c_[X_train, np.array(y_train)]
            test_arr = np.c_[X_test, np.array(y_test)]

            df_train = pd.DataFrame(train_arr)
            df_test = pd.DataFrame(test_arr)

            os.makedirs(os.path.dirname(self.data_transformation_config.transform_train_path), exist_ok=True)
            df_train.to_csv(self.data_transformation_config.transform_train_path, index = False, header = True)

            os.makedirs(os.path.dirname(self.data_transformation_config.transform_test_path), exist_ok=True)
            df_test.to_csv(self.data_transformation_config.transform_test_path, index = False, header = True)



            save_obj(file_path = self.data_transformation_config.processed_obj_filepath,
                     obj = preprocessing_obj)

            save_obj(file_path = self.data_transformation_config.fe_obj_path,
                     obj = fe_obj)
            
            return(train_arr,
                   test_arr,
                   self.data_transformation_config.processed_obj_filepath)

        except Exception as e:
            raise CustomException( e,sys)




