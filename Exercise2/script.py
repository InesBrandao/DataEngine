import pandas as pd
import pyarrow

def extract(file_name):
    return pd.read_parquet(file_name, engine = ("fastparquet"))

housePrices_data = extract("house-price.parquet")

# Check the data type of the columns of the DataFrames
#print(housePrices_data.dtypes)

# Print the shape of the DataFrame, as well as the head
print(housePrices_data.shape)
print(housePrices_data.head())
