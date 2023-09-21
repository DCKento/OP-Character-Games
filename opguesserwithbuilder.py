from flask import Flask, render_template, jsonify, request, redirect, session
import json
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Load the characters from the JSON file
with open('opwikilinksdifficulty.json', 'r') as file:
    characters = json.load(file)

def get_character_by_difficulty(difficulty):
    if difficulty == "random":
        return random.choice(characters)
    else:
        characters_of_selected_difficulty = [character for character in characters if character['difficulty'].lower() == difficulty.lower()]
        return random.choice(characters_of_selected_difficulty)
    
def get_random_character_from_easy_medium_or_hard_only():
    character = get_character_by_difficulty("random")

    while character["difficulty"] == "Extreme":
        character = get_character_by_difficulty("random")
        
    return character

# Structures to hold crew members for player 1 and player 2
crew1 = { 'Captain': None, 
          'First Mate': None, 
          'Navigator': None, 
          'Helmsman': None,
          'Fighter': None,
          'Sniper': None,
          'Cook': None,
          'Doctor': None,
          'Musician': None,
          'Shipwright': None,
          'Archeologist': None }

crew2 = { 'Captain': None, 
          'First Mate': None, 
          'Navigator': None, 
          'Helmsman': None,
          'Fighter': None,
          'Sniper': None,
          'Cook': None,
          'Doctor': None,
          'Musician': None,
          'Shipwright': None,
          'Archeologist': None }

def roll_new_characters():
    session['new_character1'] = get_random_character_from_easy_medium_or_hard_only()
    session['new_character2'] = get_random_character_from_easy_medium_or_hard_only()

@app.route('/crewbuilder', methods=['GET', 'POST'])
def crewbuilder():
    if request.method == 'POST':
        player = request.form['player']
        role = request.form['role']
        
        if player == "1" and not crew1[role]:
            crew1[role] = session['new_character1']
        elif player == "2" and not crew2[role]:
            crew2[role] = session['new_character2']
            
        return redirect('/crewbuilder')
    else:
        if 'new_character1' not in session:
            roll_new_characters()
            
        return render_template('crewbuilder.html', crew1=crew1, crew2=crew2, 
                               new_character1=session['new_character1'],
                               new_character2=session['new_character2'])

@app.route('/reroll', methods=['GET'])
def reroll():
    roll_new_characters()
    return redirect('/crewbuilder')
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