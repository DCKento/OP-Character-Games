from flask import Flask, render_template, jsonify, request
import json
import random

app = Flask(__name__)

# Load the characters from the JSON file
with open('opwikilinksdifficulty.json', 'r') as file:
    characters = json.load(file)

def get_character_by_difficulty(difficulty):
    if difficulty == "random":
        return random.choice(characters)
    else:
        characters_of_selected_difficulty = [character for character in characters if character['difficulty'].lower() == difficulty.lower()]
        return random.choice(characters_of_selected_difficulty)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/random_character', methods=['GET'])
def random_character():
    difficulty = request.args.get('difficulty', default = 'random', type = str)
    selected_character = get_character_by_difficulty(difficulty)
    return jsonify(selected_character)

if __name__ == "__main__":
    app.run(debug=True)
