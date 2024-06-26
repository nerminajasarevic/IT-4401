import pickle
import random
import os

def create_file(name):
    data = {
        "Name": name,
        "Round": 1,
        "Wins": 0,
        "Losses": 0,
        "Ratio": 0
    }
    
    with open(name + ".rps", "wb") as file:
        pickle.dump(data, file)

def save_game(name, data):
    with open(name + ".rps", "wb") as file:
        pickle.dump(data, file)

def load_game(name):
    try:
        with open(name + ".rps", "rb") as file:
            data = pickle.load(file)
        return data
    except FileNotFoundError:
        return None

def get_round(rps_info):
    return rps_info["Round"]

def initial_menu_selection():
    print("Welcome to Rock, Paper, Scissors!")
    print("1. Start New Game")
    print("2. Load Game")
    print("3. Quit")
    
    while True:
        try:
            choice = input("Enter choice: ")
            if not choice.isdigit():
                raise TypeError()
            elif choice not in ("1", "2", "3"):
                raise ValueError()
            else:
                return choice
        except TypeError:
            print("Please enter a valid integer value.")
        except ValueError:
            print("Invalid choice. Please try again.")

def play_game(name, rps_info):
    if rps_info is None:
        rps_info = {
            "Name": name,
            "Round": 1,
            "Wins": 0,
            "Losses": 0,
            "Ratio": 0
        }
    round = get_round(rps_info)

    user_choice = game_choices(round)
    computer_choice = str(random.randint(1, 3))

    user_choice = determine_object(user_choice)
    computer_choice = determine_object(computer_choice)

    round_result = determine_winner(user_choice, computer_choice)

    update_statistics(rps_info, round_result)

    end_menu(name, rps_info)

def game_choices(round_number):
    print("Round", round_number)
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    while True:
        try:
            choice = input("What will it be? ")

            if not choice.isdigit():
                raise TypeError()
            elif choice not in ("1", "2", "3"):
                raise ValueError()
            else:
                return choice
        except TypeError:
            print("Please enter a valid integer value.")
        except ValueError:
            print("Invalid choice. Please try again.")

def determine_object(choice):
    if choice == "1":
        return "Rock"
    elif choice == "2":
        return "Paper"
    elif choice == "3":
        return "Scissors"

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a tie!")
        return "tie"
    elif user_choice == "Rock":
        if computer_choice == "Paper":
            print("You lose!")
            return "loss"
        elif computer_choice == "Scissors":
            print("You win!")
            return "win"
    elif user_choice == "Paper":
        if computer_choice == "Rock":
            print("You win!")
            return "win"
        elif computer_choice == "Scissors":
            print("You lose!")
            return "loss"
    elif user_choice == "Scissors":
        if computer_choice == "Rock":
            print("You lose!")
            return "loss"
        elif computer_choice == "Paper":
            print("You win!")
            return "win"

def update_statistics(rps_info, round_result):
    rps_info["Round"] += 1

    if round_result == "win":
        rps_info["Wins"] += 1
    elif round_result == "loss":
        rps_info["Losses"] += 1

    wins = rps_info["Wins"]
    losses = rps_info["Losses"]

    if losses == 0:
        rps_info["Ratio"] = wins
    else:
        rps_info["Ratio"] = round(wins / losses, 2)

    save_game(rps_info["Name"], rps_info)

def end_menu(name, rps_info):
    print("What would you like to do?")
    print("1. Play Again")
    print("2. View Statistics")
    print("3. Quit")

    while True:
        try:
            choice = input("Enter choice: ")

            if not choice.isdigit():
                raise TypeError()
            elif choice not in ("1", "2", "3"):
                raise ValueError()
            else:
                break
        except TypeError:
            print("Please enter a valid integer value.")
        except ValueError:
            print("Invalid choice. Please try again.")

    if choice == "1":
        play_game(name, rps_info)
    elif choice == "2":
        view_statistics(name, rps_info)
    elif choice == "3":
        exit_program()

def view_statistics(name, rps_info):
    print(name + ", here are your game play statistics...")
    print("Wins:", rps_info["Wins"])
    print("Losses:", rps_info["Losses"])
    print("Win/Loss Ratio:", rps_info["Ratio"])

def exit_program():
    exit_confirm = input("Are you sure you want to exit? (y/n) ")
    if exit_confirm.lower() == "y":
        print("Thanks for playing Rock, Paper, Scissors!")
        exit()
    else:
        initial_menu_selection()

def clear_files():
    clear_confirm = input("Are you sure you want to remove all games? (y/n) ")
    if clear_confirm.lower() == "y":
        with open("RPS_DATA.txt", "w") as file:
            file.write("")
        file_list = os.listdir()
        for item in file_list:
            if item.endswith(".rps"):
                os.remove(item)
        print("Games cleared.")
    initial_menu_selection()

def initial_menu(name, rps_info):
    repeat = True

    while repeat:
        choice = initial_menu_selection()

        if choice == "1":
            name = input("What is your name? ")
            rps_info = load_game(name)
            if rps_info is not None:
                print("Hello, {}. Let's play!".format(name))
            else:
                create_file(name)

            play_game(name, rps_info)

        elif choice == "2":
            name = input("Whose game would you like to load? ")
            rps_info = load_game(name)

            if rps_info is None:
                print("No games found for '{}'.".format(name))
            else:
                print("Welcome back, {}. Let's play!".format(name))
                play_game(name, rps_info)

        elif choice == "3":
            repeat = False
            print("Goodbye!")

        elif choice == "4":
            clear_files()

    print("Thanks for playing Rock, Paper, Scissors!")

def main():
    name = ""
    rps_info = {}
    initial_menu(name, rps_info)

main()
