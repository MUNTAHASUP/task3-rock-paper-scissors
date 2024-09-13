import sys
import random
import secrets
import hmac
import hashlib


class KeyGenerator:
    @staticmethod
    def generate_key():
        # Generate a secure random key of 256 bits
        return secrets.token_hex(32)  # 32 bytes = 256 bits


class HMACGenerator:
    @staticmethod
    def generate_hmac(key, message):
        # Generate HMAC using SHA256
        return hmac.new(bytes.fromhex(key), message.encode(), hashlib.sha256).hexdigest()


class GameRules:
    def __init__(self, moves):
        self.moves = moves
        self.num_moves = len(moves)

    def determine_winner(self, player_move, computer_move):
        player_index = self.moves.index(player_move)
        computer_index = self.moves.index(computer_move)

        if player_index == computer_index:
            return "Draw"

        half = self.num_moves // 2
        winning_indices = [(computer_index + i + 1) % self.num_moves for i in range(half)]

        if player_index in winning_indices:
            return "You win!"
        else:
            return "You lose!"


class HelpTableGenerator:
    def __init__(self, moves):
        self.moves = moves

    def generate_help_table(self):
        n = len(self.moves)
        table = [[""] * (n + 1) for _ in range(n + 1)]
        
        # Set headers
        table[0][1:] = self.moves
        for i in range(1, n + 1):
            table[i][0] = self.moves[i - 1]

        # Fill the table with Win/Lose/Draw
        rules = GameRules(self.moves)
        for i in range(n):
            for j in range(n):
                if i == j:
                    table[i + 1][j + 1] = "Draw"
                else:
                    result = rules.determine_winner(self.moves[i], self.moves[j])
                    table[i + 1][j + 1] = "Win" if result == "You win!" else "Lose"

        # Display table
        for row in table:
            print("\t".join(row))


def validate_moves(moves):
    if len(moves) < 3 or len(moves) % 2 == 0:
        raise ValueError("The number of moves must be an odd number ≥ 3.")
    if len(set(moves)) != len(moves):
        raise ValueError("Moves must be unique and non-repeating.")


def main():
    # Get moves from command line arguments
    moves = sys.argv[1:]
    try:
        validate_moves(moves)
    except ValueError as e:
        print(f"Error: {e}")
        print("Example: python game.py rock paper scissors")
        sys.exit(1)

    # Generate key and computer's move
    key = KeyGenerator.generate_key()
    computer_move = random.choice(moves)
    hmac_value = HMACGenerator.generate_hmac(key, computer_move)
    
    print(f"HMAC: {hmac_value}")
    print("Available moves:")
    for i, move in enumerate(moves, 1):
        print(f"{i} - {move}")
    print("0 - exit")
    print("? - help")

    # Main game loop
    while True:
        choice = input("Enter your move: ").strip()

        if choice == '0':
            print("Game exited.")
            break
        elif choice == '?':
            HelpTableGenerator(moves).generate_help_table()
            continue

        try:
            choice = int(choice)
            if choice < 1 or choice > len(moves):
                raise ValueError
            player_move = moves[choice - 1]
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the available moves or '?' for help.")
            continue

        # Determine the result
        rules = GameRules(moves)
        result = rules.determine_winner(player_move, computer_move)
        print(f"Your move: {player_move}")
        print(f"Computer move: {computer_move}")
        print(f"{result}")
        print(f"HMAC key: {key}")
        break


if __name__ == "__main__":
    main()
