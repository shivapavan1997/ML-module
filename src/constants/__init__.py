import os ,sys
from datetime import datetime

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

CURENT_TIME_STAMP=get_current_time_stamp()

DATA_DIR_KEY="finalTrain.csv"
DATA_DIR="Data"
ROOT_DIR_KEY=os.getcwd()

#CurrentWorkingDIR/Data/finalTrain.csv

ARTIFACT_DIR_KEY="Artifact" #Define folder name

#Data ingestion related variable
DATA_INGESTION_KEY="data_ingestion"
DATA_INGESTION_RAW_DATA_DIR="raw_data_dir"
RAW_DATA_DIR_KEY="raw.csv"
DATA_INGESTION_INGESTED_DATA_DIR_KEY="ingested_dir"
TRAIN_DATA_DIR_KEY="train.csv"
TEST_DATA_DIR_KEY="test.csv"


#Data transformation related variable
#artifacts/data_transformation/processor->processor.pkl and transformation->train.csv and test.csv

DATA_TRANSFOMRATION_ARTIFACT="data_transformation"
DATA_PREPROCESSED_DIR="processor"
DATA_TRANSFORMATION_PROCESSING_OBJ="processor.pkl"
DATA_TRANSFORM_DIR="transformation"
TRANSFORM_TRAIN_DIR_KEY="train.csv"
TRANSFORM_TEST_DIR_KEY="test.csv"


## Model Trainer

MODEL_TRAINER_KEY="model_trainer"
MODEL_OBJECT="model.pkl"
