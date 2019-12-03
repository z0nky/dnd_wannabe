import dice

def where_to_go():
    print("City road leads towards river and mine. But you have spotted sign saying 'Mines closed.'. You can also stay in the city")
    destination = input("Where will you travel? (river/stay) ")
    if destination == "river":
        return "river"
    elif destination == "stay":
        return "stay"
    else:
        print("Please input 'river' or 'stay'!")
        where_to_go()


def where_to_go_river():
    print("The road has two turn. One towards the mine, which is closed and one towards city.")
    destination = input("Do you want to go to the city or stay at the river? (city/stay) ")
    if destination == "city":
        return "city"
    elif destination == "stay":
        return "stay"
    else:
        print("Please input 'city' or 'stay'!")
        where_to_go_river()


def encounter(player):
    player_roll = dice.roll_dice() + player.weapon
    opponent_roll = dice.roll_dice()
    if player_roll > opponent_roll:
        print(f"{player.name} has rolled {player_roll} and opponent has rolled {opponent_roll}. {player.name} wins this round!")
        return "Player win"
    elif player_roll < opponent_roll:
        print(f"{player.name} has rolled {player_roll} and opponent has rolled {opponent_roll}. {player.name} lost this round!")
        return "Opponent win"
    else:
        print(f"{player.name} has rolled {player_roll} and opponent has rolled {opponent_roll}. This round ended with draw!")
        return "Draw"


def encounter_disadvantage(player):
    player_roll = dice.roll_dice() + player.weapon
    opponent_roll = 0
    opponent_roll1 = dice.roll_dice_1k12()
    opponent_roll2 = dice.roll_dice_1k12()
    if opponent_roll1 > opponent_roll2:
        opponent_roll = opponent_roll1
    else:
        opponent_roll = opponent_roll2
    if player_roll > opponent_roll:
        print(
            f"{player.name} has rolled {player_roll} and opponent has rolled {opponent_roll}. {player.name} wins this round!")
        return "Player win"
    elif player_roll < opponent_roll:
        print(
            f"{player.name} has rolled {player_roll} and opponent has rolled {opponent_roll}. {player.name} lost this round!")
        return "Opponent win"
    else:
        print(
            f"{player.name} has rolled {player_roll} and opponent has rolled {opponent_roll}. This round ended with draw!")
        return "Draw"

def end_game(player):
    player_roll = dice.roll_dice() + player.weapon
    opponent_roll = 0
    opponent_roll1 = dice.roll_dice_1k12() + player.weapon
    opponent_roll2 = dice.roll_dice_1k12() + player.weapon
    if opponent_roll1 > opponent_roll2:
        opponent_roll = opponent_roll1
    else:
        opponent_roll = opponent_roll2
    if player_roll > opponent_roll:
        print(
            f"{player.name} has rolled {player_roll} and Black Knight has rolled {opponent_roll}. {player.name} wins this round!")
        return "Player win"
    elif player_roll < opponent_roll:
        print(
            f"{player.name} has rolled {player_roll} and Black Knight has rolled {opponent_roll}. {player.name} lost this round!")
        return "Black Knight win"
    else:
        print(
            f"{player.name} has rolled {player_roll} and Black Knight has rolled {opponent_roll}. This round ended with draw!")
        return "Draw"