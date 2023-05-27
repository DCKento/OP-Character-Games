import json
import random

# Opening the JSON file containing the OP character wiki links, loading the contents as "characters" variable
with open('opwikilinks.json', 'r') as file:
    characters = json.load(file)

#selected_caracter variable uses the random.choice function to randomly select one chracter from the "characters" variable
selected_character = random.choice(characters)

#print the selected character to the terminal as output
print(f"Selected Top 100 Character: {selected_character}")
