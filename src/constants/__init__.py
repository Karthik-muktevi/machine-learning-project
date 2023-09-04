import sys,os
from datetime import datetime

def get_current_timestamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

CURRENT_TIMESTAMP = get_current_timestamp()

ROOT_DIR = os.getcwd()
DATA_DIR = "Data"
DATA_DIR_KEY = "finalTrain.csv"

ARTIFACT_DIR = "Artifact"

#Data ingestion related variable
DATA_INGESTION_DIR ="data_ingestion"
RAW_DATA_DIR = "raw_data_dir"
INGESTED_DATA_DIR = "ingested_dir"
RAW_DATA_DIR_KEY = "raw.csv"
TRAIN_DATA_DIR_KEY = "train.csv"
TEST_DATA_DIR_KEY = "test.csv"

# Data Transformation related variable

TRANSFORMATION_ARTIFACT_DIR = "data_transformation"
DATA_PREPROCESSED_DIR = "processor"
OBJ_PREPROCESSED = "processor.pkl"
TRANSFORM_DIR = "transformation"
TRANSFORM_TRAIN_DIR_KEY = "train.csv"
TRANSFORM_TEST_DIR_KEY = "test.csv"

#Model training

MODEL_DIR = "models"
MODEL_OBJECT = "model.pkl"