import json
import pandas as pd

def extract(file_path):
    return pd.read_json(file_path, orient = "columns")

raw_data_eg = extract("raw_stock_data.json")

# Output the head of the DataFrame
print(raw_data_eg.head())
