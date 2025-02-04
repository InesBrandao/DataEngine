import pandas as pd

def extract(fileName):
    print(f"Extracting data from {fileName}")
    # Read a CSV with a path stored using file_name into memory
    return pd.read_csv(fileName)

def transform_onlyUS (dataFrame):
    #select only recovered and usa from JH
    onlyUS_data = dataFrame.loc[dataFrame["Country/Region"] == "US"]
    return onlyUS_data

def dropColumns (dataUS):
    cleanData_US = dataUS.drop(columns = ["Country/Region", "Province/State", "Confirmed", "Deaths"])
    return cleanData_US

def mergeTwoDataFrames (og_data, extra_data):
    #convert the 2 date columns into datetime appropriate:
    og_data["date"] = pd.to_datetime(og_data["date"])
    extra_data["Date"] = pd.to_datetime(extra_data["Date"])
    # do left merge of 2 dataframes
    mergedData = og_data.merge(extra_data, how = "left", left_on="date", right_on="Date")
    return mergedData

file_name = "us.csv"
covidData = extract(file_name)

file_jH = "other.csv"
otherData = extract(file_jH)
cleanOtherData = transform_onlyUS(otherData)
cleaned_US_Data = dropColumns (cleanOtherData)
#print(cleanOtherData.shape)
#print(cleaned_US_Data.head())
#print(covidData.head())

covidMergedData = mergeTwoDataFrames(covidData, cleaned_US_Data)
#print(covidMergedData.head())

#remove Date column
covidMergedData1 = covidMergedData.drop(columns = ["Date"])
#print(covidMergedData1.head())
#clean Na values in rows
cleanedData = covidMergedData1.dropna(axis="index")
#print(cleanedData.head())

#change float into integer then export to python file (.py)
#convert "Recovered" column from float to integer
cleanedData["Recovered"] = cleanedData["Recovered"].astype(int)
print(cleanedData.head())
