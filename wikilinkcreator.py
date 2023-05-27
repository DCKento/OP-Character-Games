import json

# Load the data from the file
with open('opcharacters.json', 'r') as infile:
    data = json.load(infile)

base_url = "https://onepiece.fandom.com/wiki/"

# Transform the data
updated_data = [base_url + character for character in data]

# Write the transformed data to a new file
with open('opwikilinks.json', 'w') as outfile:
    json.dump(updated_data, outfile, indent=4)
