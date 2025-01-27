import pandas as pd
import pyarrow

def extract(file_name):
    return pd.read_parquet(file_name, engine = ("fastparquet"))

def transform(raw_data):
    #only keep rows with area smaller than 3000 msqd
    clean_data = raw_data.loc[raw_data["area"] < 3000, ["price", "area", "bedrooms", "bathrooms", "parking"]]

    #only keep rows with one parking lot space
    clean_data = clean_data.loc[clean_data["parking"] == 1, :]
    #return the filtered dataFrame
    return clean_data

def load(cleaned_data):
    cleaned_data.to_csv("affordable_options.csv", index = False)
    
    
housePrices_data = extract("house-price.parquet")
clean_data = transform(housePrices_data)

load(clean_data)

# Check the data type of the columns of the DataFrames
#print(housePrices_data.dtypes)

# Print the shape of the DataFrame, as well as the head
#print(housePrices_data.shape)
#print(housePrices_data.head())

