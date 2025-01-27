import pandas as pd
import pyarrow

def extract(file_name):
    return pd.read_parquet(file_name, engine = ("fastparquet"))

def transform(raw_data):
    #only keep rows with area smaller than 3000 msqd
    clean_data = raw_data.loc[raw_data["area"] < 3000, :]

    #only keep columns "price", "area", bedrooms", "bathrooms" and "parking"
    clean_data = clean_data.loc[:, ["price", "area", "bedrooms", "bathrooms", "parking"]]

    #only keep rows with one parking lot space
    clean_data = clean_data.loc[clean_data["parking"] == 1, :]
    #return the filtered dataFrame
    return clean_data


    
housePrices_data = extract("house-price.parquet")
print(transform(housePrices_data))

# Check the data type of the columns of the DataFrames
#print(housePrices_data.dtypes)

# Print the shape of the DataFrame, as well as the head
#print(housePrices_data.shape)
#print(housePrices_data.head())

