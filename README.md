# OP-Character-Games

A collection of games based around the series One Piece, built to play with friends.

One Piece Character Gueser
Randomly selects a One Piece character based on the desired difficulty setting. Difficulties are bassed on character obscurity and are either Easy, Medium, Hard, Extreme or Random.

There are currently 380 different characters that could be selected, with a difficulty selector enabled. Once a character is selected, the wikilink also supplied.

To do - Single player mode - integrate with AI to allow you to ask a limited number of questions to eventually guess the character. Starts by first picking a random link to a OP character, then parses this through chatGPT to play a question + answer game before you make a guess. ChatGPT will answer only with "yes", "no" or "don't know" based on the information contained within the wikipedia page for that character. There are 10 questions a player can have before making a final guess.

One Piece Crew Builderr
Build the best crew against a friend.

- Two random One Piece characters are generated, one for each player. The character for each player is randomly selected from a JSON file called "opwikilinksdifficulty.json". Both players are expected to get different characters.
- On a "Crew" there are 11 roles. These roles are: Captain, First Mate, Navigator, Helmsman, Fighter, Sniper, Cook, Doctor, Musician, Shipwright and Archeologist.
- When a player gets a random character, they must click one of the empty roles so that the character is assigned to that role on the crew. Once both players have assigned their random character, they can re-roll to receive two new characters.
- Once a role has been filled, it cannot be overwritten. The next character must be assigned to one of the remaining empty roles.
- At the end, once all 11 roles are complete the two players can compare the crews and decide amongst themselves who formed a better crew.

# GPT Prompt

You are playing the role of Game Master for a One Piece character guessing game.

There is a single One Piece character that I am trying to guess. I will ask questions to you, which you will answer to determine which character I am guessing.

The rules are as follows:

You MUST only reply with "yes" or "no". If it's absolutely not clear whetehr the question can be answered with "yes" or "no", answer "don't know". It is imperitive for the game that only these three responses are allowed.

The character I am guessing is: {randomly selected wikilink}. Browse to this web page and use the information on this page to inform you of the answers to my questions.
