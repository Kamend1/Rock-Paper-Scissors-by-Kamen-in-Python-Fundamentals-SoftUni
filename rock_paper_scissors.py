import random
import termcolor

player_name = input("Please write your name: ")
moves = {"r": "rock", "p": "paper", "s": "scissors"}
restart = ""
score_player = 0
score_computer = 0

while True:

    player_move = input(f'Hello {player_name}! Choose [r]ock, [p]aper, or [s]cissors: ')
    try:
        if player_move not in moves:
            raise ValueError("Invalid Input. Try again...")
    except ValueError:
        print(termcolor.colored("Invalid Input. Try again...", "red"))
        continue

    player_move = moves[player_move]

    computer_random_number = random.randint(1, 3)
    computer_move = ""

    if computer_random_number == 1:
        computer_move = "r"
        computer_move = moves[computer_move]
    elif computer_random_number == 2:
        computer_move = "p"
        computer_move = moves[computer_move]
    elif computer_random_number == 3:
        computer_move = "s"
        computer_move = moves[computer_move]

    print(f"The computer chose {computer_move}.")

    if (player_move == "rock" and computer_move == "scissors") or \
        (player_move == "paper" and computer_move == "rock") or \
        (player_move == "scissors" and computer_move == "paper"):
        termcolor.cprint("You Win!", color="green")
        score_player += 1
    elif player_move == computer_move:
        print(termcolor.colored("Draw!", color="yellow"))
    else:
        print(termcolor.colored("You Lose!", color="red"))
        score_computer += 1

    print(f"{player_name} {score_player} vs. Computer {score_computer}")

    restart = input("Type [yes] if you would like to play again and [no] to exit: ")
    while restart not in ['yes', 'no']:
        print("Invalid Input. Try again...")
        restart = input("Type [yes] if you would like to play again and [no] to exit: ")
    if restart == "no":
        print("Thank you for playing!")
        break

    restart = ""
