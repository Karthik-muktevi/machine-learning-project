from src.pipeline.prediction_pipeline import CustomData,PredictPipeline
import streamlit as st
import pandas as pd
from src.pipeline.prediction_pipeline import CustomData, PredictPipeline
import os,sys
from Prediction.batch import BatchPrediction
from Prediction.batch import *
from src.logger import logging
from src.components.data_transformation import DataTransformationConfig
from src.config.configuration import *
from src.pipeline.training_pipeline import Train

feature_engineering_file_path = FE_OBJ_FILEPATH
transformer_file_path = PREPROCESSING_OBJ_FILEPATH
model_file_path = MODEL_FILEPATH

st.image("templates/zomato_picture.jpg")
st.title('Delievery time prediction')
st.header('select either single prediction or batch prediction')
x = st.selectbox(label="select type of prediction",options= (['single prediction','batch prediction']))
if x == 'single prediction':
    data = CustomData(
        Delivery_person_Age = st.number_input(label='Delivery_person_Age'),
        Delivery_person_Ratings = st.number_input(label='Delivery_person_Ratings'),
        Weather_conditions = st.selectbox(label='Weather_conditions',options=['Sunny','Cloudy','Windy','Fog','Sandstorms','Stormy']),
        Road_traffic_density = st.selectbox(label='Road_traffic_density',options=['Low','Medium','High','Jam']),
        Vehicle_condition =  st.selectbox(label='Vehicle_condition',options=[0,1,2,3]),
        multiple_deliveries = st.selectbox(label ='multiple_deliveries',options=[0,1,2,3]),
        distance = st.number_input(label='distance'),
        Type_of_order = st.selectbox(label='Type_of_order',options=['Snack' 'Meal' 'Drinks' 'Buffet']),
        Type_of_vehicle = st.selectbox(label='Type_of_vehicle',options=['motorcycle', 'scooter', 'electric_scooter', 'bicycle']),
        Festival = st.selectbox(label='Festival',options=['No','Yes']),
        City = st.selectbox(label='City',options=['Metropolitian','Urban','Semi-Urban'])
    )
        
    final_new_data = data.get_data_as_dataframe()
    predict_pipeline = PredictPipeline()
    pred = predict_pipeline.predict(final_new_data)
    result = int(pred[0])
    submit = st.button(label='Get predictions')
    if submit:
        st.write(f"The delievery will come in {result} mins")
        
        
elif x == 'batch prediction':
     st.button(label="file upload")
     uploaded_file = st.file_uploader(label="Choose a file", type = ['csv'])
     if uploaded_file is not None:
        logging.info("CSV received and Uploaded")

            # Perform batch prediction using the uploaded file
     submit = st.button(label='Get prediction file')
     if submit:
        batch = BatchPrediction(uploaded_file,
                                    model_file_path,
                                    transformer_file_path,
                                    feature_engineering_file_path)
        batch.start_batch_prediction()
        
        


        






