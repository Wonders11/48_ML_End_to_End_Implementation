from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData

# creating object of class
custdataobject = CustomData(2.67,62.6,57.0,4.29,4.26,2.67,"Ideal","G","VVS1") # the sequence of data passed should be 
# same as mentioned in CustomData class in prediction_pipeline.py file

data = custdataobject.get_data_as_dataframe()

print(data)