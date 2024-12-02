import sys
import random
from enum import Enum


def gn(name='PlayerOne'):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_gn():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        playerchoice = input(
            f"\n{name}, gues which number I'm thinking if... 1, 2, or 3.\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_gn()

        player = int(playerchoice)

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(f"\n{name}, you chose {int(playerchoice)}")
        print(
            f"I was thinking about {int(computerchoice)}.\n"
        )

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            if player == computer:
                player_wins += 1
                return f"🎉 {name}, you win!"
            else:
                python_wins += 1
                return f"Sorry, {name}. Better luck next time. 🥲"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(
            f"\nYour winning percentage: {player_wins / game_count * 100:.2f}%")

        print(f"\nPlay again, {name}?")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_gn()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}! 👋\n")
            else:
                return

    return play_gn


guess_my_number = gn()
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    guess_my_number = gn(args.name)
    guess_my_number()
