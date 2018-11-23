# Word Whiz
Word Whiz is a fun and educational word guessing game, similar to the "Hangman" game, whereby the computer challenges a guesser to guess a secret word. The computer gives the guesses the length of the word, in which the location of the possible letters are denoted by underscores, and the guesser must try to guess the word one letter at a time. If the guesser guesses a correct letter, the computer reveals all occurences of that letter to the guesser. The guesser must guess the word with less than 6 incorrect guess attempts to win the game. The computer wins if the guesser runs out of guess attempts.  

Points are awarded for guessing letters correctly, even if the player loses, in order to encourage the player to continue guessing and learn new words. Fewer points are deducted if the player gueses incorrectly. A bar at the bottom of the page shows the proportion of guesses remaining. The player can adjust the difficulty level on a scale of 1-10 to receive more or less challenging words.


## Contents
* [Technology Stack](#technology-stack)
* [Dependencies](#dependencies)
* [Game Rules](#game-rules)
* [Game Guidelines](#game-guidelines)
* [Features](#features)
* [Design Decisions](#design-decisions)
* [Setup](#setup)
* [Version 2.0](#version-2.0)
* [About the Developer](#about-the-developer)

### Technology Stack
* Python3
* Flask
* Jinja2
* SQLAlchemy
* JavaScript (AJAX, JSON, jQuery)
* HTML/CSS
* Boostrap

### DEPENDENCIES
* API: LinkedIn's Word API

### GAME RULES
* The computer will pick a secret dictionary word at the beginning of the game
* The computer deducts one attempt each time a guessed letter is not in the word
* The computer wins the game if the guesser picks 6 letters that are not in the word, and the guesser loses
* The guesser wins the game if they guess all letters in the word, and choose less than 6 letters that are not in the word

### GAME GUIDELINES
* The guesser can adjust difficulty level on a scale from 1-10, with 10 providing the most difficult words.
* The computer sets difficulty level at 3 when the player logs in, but when the player adjusts difficulty level, it is maintained throughput the session.
* The computer awards points for each correctly guessed letter.
* The computer awards more points at higher word difficulty levels.
* The computer will still award points if the player loses the game, but does not award points if the player does not finish the game.

### SETUP

1. Clone the repository to a local directoy 
2. After acitivating the virtual environment:
	* `pip3 install requirements.txt`
3. Create the database:
   * `createdb scoresdb`
4. Run the server:
  * `python server.py`
  * `localhost:5000 in the browser window`
5. Check tests by running the following:
	 * `python3 test_server.py`
	 * `python3 test_game.py`


### VERSION 2.0
Coming soon!

* The computer shows the score dynamically while user is playing the game.
* The player can guess the entire word at once.
* The computer gives a hint to the player by proviging the word's dictinary definition.
* At the end of every game, the computer will display the word's definition to the player.
* The player can adjust minimum and maximum length of the word.
* The player can adjust the difficulty level in the profile. 
* The player will not be able to receive the same word more than once. 

### About the Developer
Jessica is a software engineer and former clinical dietitian based out of San Francisco.