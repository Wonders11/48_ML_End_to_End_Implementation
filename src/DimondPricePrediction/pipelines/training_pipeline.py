# importing data ingestion class
from src.DimondPricePrediction.components.data_ingestion import DataIngestion

import os
import sys
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customexception
import pandas as pd

# creation of data ingestion object
obj = DataIngestion() # once we create object of data ingestion, configuration object will also be created

# calling initiate_data_ingestion function
obj.initiate_data_ingestion()