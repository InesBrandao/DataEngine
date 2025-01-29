import pandas as pd
import json

def extract(file_path):
    return pd.read_json(file_path, orient = "items")

school = extract("school_raw_data.json")

#print(school.head())

# Parse the street_address from the dictionary
streetAddress = school.get("street_address")
city = school.get("city")
# Parse the scores dictionary
scores = school.get("scores")

# Try to parse the math, reading and writing values from scores
math_score = scores.get("math", 0)
reading_score = scores.get("reading", 0)
dancing_score = scores.get("dancing", 0)
print(f"City: {city}")
#print(f"Street Address: {streetAddress}")
print(f"Math: {math_score}, Reading: {reading_score}, Dancing: {dancing_score}")
