import random

def get_user_choice():
    choice = input("\nChoose one (rock, paper, or scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose again.")
        choice = input("Your choice: ").lower()
    return choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    tie_score = 0

    print("🎮 Welcome to Rock-Paper-Scissors!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\n🧍 You chose: {user_choice}")
        print(f"💻 Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == "user":
            print("✅ You win this round!")
            user_score += 1
        elif winner == "computer":
            print("❌ Computer wins this round!")
            computer_score += 1
        else:
            print("🤝 It's a tie!")
            tie_score += 1

        print(f"\n📊 Scoreboard:")
        print(f"You: {user_score} | Computer: {computer_score} | Ties: {tie_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\n👋 Thanks for playing!")
            break

# Run the game
play_game()
