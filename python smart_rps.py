import random

# Function to get the move that beats the given move
def get_winning_move(move):
    return {"rock": "paper", "paper": "scissors", "scissors": "rock"}[move]

# Predict the player's next move based on their history
def predict_next_move(history):
    if not history:
        return random.choice(["rock", "paper", "scissors"])
    
    last_move = history[-1]
    next_moves = {"rock": 0, "paper": 0, "scissors": 0}

    # Count what the player tends to play after a specific move
    for i in range(len(history) - 1):
        if history[i] == last_move:
            next_moves[history[i + 1]] += 1

    # Predict the player's next move
    predicted_move = max(next_moves, key=next_moves.get)
    return get_winning_move(predicted_move)  # Counter it

# Main game function
def smart_rps():
    print("Welcome to Smart Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to stop.\n")

    user_history = []
    score = {"user": 0, "computer": 0, "tie": 0}

    while True:
        user = input("Your move: ").lower()
        if user == "quit":
            print("\nFinal Score:")
            print(f"You: {score['user']} | Computer: {score['computer']} | Ties: {score['tie']}")
            print("Thanks for playing!")
            break

        if user not in ["rock", "paper", "scissors"]:
            print("Invalid input. Try again.\n")
            continue

        computer = predict_next_move(user_history)
        user_history.append(user)

        print(f"Computer chose: {computer}")

        if user == computer:
            print("It's a tie!\n")
            score["tie"] += 1
        elif get_winning_move(user) == computer:
            print("Computer wins!\n")
            score["computer"] += 1
        else:
            print("You win!\n")
            score["user"] += 1

smart_rps()
