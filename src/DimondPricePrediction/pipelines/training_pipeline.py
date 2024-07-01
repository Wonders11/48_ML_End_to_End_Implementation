# importing data ingestion class
from src.DimondPricePrediction.components.data_ingestion import DataIngestion
from src.DimondPricePrediction.components.data_transformation import DataTransformation
from src.DimondPricePrediction.components.model_trainer import ModelTrainer

import os
import sys
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customexception
import pandas as pd

# creation of data ingestion object
obj = DataIngestion() # once we create object of data ingestion, configuration object will also be created
# calling initiate_data_ingestion function
train_data_path, test_data_path = obj.initiate_data_ingestion()

# creation of data transformation object
data_transformation = DataTransformation()
train_arr, test_arr = data_transformation.initialize_data_transformation(train_data_path,test_data_path)

# creation of Model Trainer object
model_trainer_obj = ModelTrainer()
model_trainer_obj.initiate_model_training(train_arr,test_arr)