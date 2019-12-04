import gascii
import os


def typo():
    print(gascii.typo())
    input("To proceed press any key and ENTER.")


def my_stats(player):
    print(player)
    input("To proceed press any key and ENTER.")


def clean_up():
    return os.system('cls')


def game_over(player):
    print(gascii.you_died())
    he_ded = input(f"Well better luck next time {player.name}. Do you want to try again? (yes/no) ").lower()
    if he_ded == "yes" or he_ded == "y":
        return "re_do"
    elif he_ded == "stats":
        print(f"Are you kidding me? This is no time to check your stats. Here is one that matters: {player.life} hp left!")
        game_over(player)
    elif he_ded == "no" or he_ded == "n":
        return "gg"
    else:
        typo()
        game_over(player)
