import sys
import random
from enum import Enum

game_stats = {
    "game_count": 0,
    "winning_count": 0,
    "loosing_count": 0,
    "tie_count": 0}


def play_rps():

    class RPS(Enum):
        Rock = 1
        Paper = 2
        Scissors = 3

    playerchoice = input(
        "\nEnter...\n1 for Rock,\n2 for Paper, or \n3 or Scissors:\n\n")

    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3.")
        return play_rps()

    player = int(playerchoice)

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("\nYou chose " + str(RPS(player)).replace("RPS.", "") + ".")
    print("Python chose " + str(RPS(computer)).replace("RPS.", "") + ".\n")

    global game_stats

    def decide_winner(player, computer):
        game_stats["game_count"] += 1
        if player == 1 and computer == 3:
            game_stats["winning_count"] += 1
            return "🍀 You win!"
        elif player == 2 and computer == 1:
            game_stats["winning_count"] += 1
            return "🍀 You win!"
        elif player == 3 and computer == 2:
            game_stats["winning_count"] += 1
            return "🍀 You win!"
        elif player == computer:
            game_stats["tie_count"] += 1
            return "😐 Tie game!"
        else:
            game_stats["loosing_count"] += 1
            return "😎 Python wis!"

    game_result = decide_winner(player, computer)

    print(game_result)

    # global game_count
    # game_count += 1

    print("\nGame count: " + str(game_stats["game_count"]))
    print("\nWinning count: " + str(game_stats["winning_count"]))
    print("\nLoosing count: " + str(game_stats["loosing_count"]))
    print("\nTie count: " + str(game_stats["tie_count"]))

    print("\nPlay again?")

    while True:
        playagain = input("\nY for Yes or \nQ for Quit\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n👻")
        print("Thank you for playin!\n")
        sys.exit("Bye! 👹")


play_rps()
