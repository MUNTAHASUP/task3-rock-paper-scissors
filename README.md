**Generalized Rock-Paper-Scissors Game**
This Python script implements a generalized version of Rock-Paper-Scissors that supports an arbitrary number of moves. The game features cryptographic fairness through HMAC verification and secure key generation.

**Features**
Customizable Moves: Supports any odd number of moves (≥ 3).
Cryptographic Fairness: Uses a secure random key and HMAC to ensure the computer's move is unaltered.
Dynamic Help Table: Generates an ASCII table showing win/lose/draw outcomes for each move.
Error Handling: Provides clear error messages and instructions for correct input.
**Running the Game**
To run the game, use the following command:

python game.py move1 move2 move3 ...
Replace move1, move2, move3, etc., with your chosen moves.

**Example**
HMAC: 9ED68097B2D5D9A968E85BD7094C75D00F96680DC43CDD6918168A8F50DE8507
Available moves:
1 - rock
2 - paper
3 - scissors
4 - lizard
5 - spock
0 - exit
? - help
Enter your move: 2
Your move: paper
Computer move: rock
You win!
HMAC key: BD9BE48334BB9C5EC263953DA54727F707E95544739FCE7359C267E734E380A2

**Project Structure**
game.py: Main script for game logic and user interaction.
hmac_generator.py: Handles key generation and HMAC calculation.
rules.py: Defines game rules for determining winners.
help_table.py: Generates the help table.

**Technologies Used**
Python 3.x: Programming language.
Hashlib: For HMAC and SHA-256.
OS and Sys Libraries: For command-line argument handling.

**Contributing**
Feel free to fork the repository and submit pull requests. Ensure code follows the existing style and includes tests.

**Contact**
GitHub: Muntaharsup
Email: ahasanmuntaha@gmail.com
**License**
This project is licensed under the MIT License.
