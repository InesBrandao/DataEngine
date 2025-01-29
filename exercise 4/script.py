import json
import pandas as pd

def extract(file_path):
    return pd.read_json(file_path, orient = "items")

raw_testing_scores_keys = []
raw_testing_scores_values = []

raw_testing_scores = extract("nested_school_scores.json")

# Iterate through the keys of the raw_testing_scores dictionary
#for school_id in raw_testing_scores.keys():
  	# Append each key to the raw_testing_scores_keys list
#	raw_testing_scores_keys.append(school_id)
    
#print(raw_testing_scores_keys[0:3])


# Iterate through the keys and values (at the same time) of the raw_testing_scores dictionary

for school_id, school_info in raw_testing_scores.items():
	raw_testing_scores_keys.append(school_id)
	raw_testing_scores_values.append(school_info)

print(raw_testing_scores_keys[0:4])
print(raw_testing_scores_values[0:4])
