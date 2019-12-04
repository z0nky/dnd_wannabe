import random


def roll_dice():
    dice1k6 = random.randint(1, 6)
    return dice1k6


def roll_dice_1k12():
    dice1k12 = random.randint(1, 12)
    return dice1k12


def roll_dice_2k12():
    dice1 = random.randint(1, 12)
    dice2 = random.randint(1, 12)
    return dice1 if dice1 >= dice2 else dice2
