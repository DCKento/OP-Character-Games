from flask import Flask, render_template, jsonify
import json
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/random_character', methods=['GET'])
def random_character():
    with open('opwikilinks.json', 'r') as file:
        characters = json.load(file)
    selected_character = random.choice(characters)
    return jsonify({'character': selected_character})

if __name__ == "__main__":
    app.run(debug=True)