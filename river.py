import dice
import moving
import city
import gascii
import commands


def cave_wolf_encounter(player):
    opponent_life = 5
    while player.life > 0 and opponent_life > 0:
        if moving.encounter(player) == "Player win":
            opponent_life -= player.weapon
            print(
                f"{player.name} hits wolf for {player.weapon} points! Wolf has {opponent_life} hit points left.")
        elif moving.encounter(player) == "Opponent win":
            player.life -= 10
            print(f"{player.name} takes hit for 10 points. You have {player.life} hit points left.")
        else:
            print(moving.encounter(player))
    if player.life == 0:
        print("Oh no, you are dead! X_X")
    elif opponent_life <= 0:
        prize = dice.roll_dice() * 11
        player.money += prize
        print(f"{player.name} has killed wolf and found {prize} gold coins. "
              f"Now {player.name} has {player.money} gold coins and {player.life}/100 hit points left.")
        print(f"{player.name} feeling strong walks back towards river bank.")
        river_cave_02(player)


def river_troll_fight1(player):
    opponent_life = 10
    while player.life > 0 and opponent_life > 0:
        if moving.encounter_disadvantage(player) == "Player win":
            opponent_life -= player.weapon
            print(
                f"{player.name} hits troll for {player.weapon} points! Troll has {opponent_life} hit points left.")
        elif moving.encounter_disadvantage(player) == "Opponent win":
            player.life -= 10
            print(f"{player.name} takes hit for 10 points. You have {player.life} hit points left.")
        else:
            print(moving.encounter_disadvantage(player))
    if player.life == 0:
        print("Oh no, you are dead! X_X")
    elif opponent_life <= 0:
        prize = dice.roll_dice() * 20
        player.money += prize
        print(f"{player.name} has killed troll and found {prize} gold coins. "
              f"Now {player.name} has {player.money} gold coins and {player.life}/100 hit points left.")
        print(f"{player.name} feeling strong walks back towards river bank.")
        player.quest = 2
        print(f"Exhausted {player.name} leaves the cave. It's time to go back to the city to get reward from the order, isn't it?")
        river_direction(player)


def river_troll_fight2(player):
    opponent_life = 10
    while player.life > 0 and opponent_life > 0:
        if moving.encounter(player) == "Player win":
            opponent_life -= player.weapon
            print(
                f"{player.name} hits troll for {player.weapon} points! Troll has {opponent_life} hit points left.")
        elif moving.encounter(player) == "Opponent win":
            player.life -= 10
            print(f"{player.name} takes hit for 10 points. You have {player.life} hit points left.")
        else:
            print(moving.encounter(player))
    if player.life == 0:
        print("Oh no, you are dead! X_X")
    elif opponent_life <= 0:
        prize = dice.roll_dice() * 20
        player.money += prize
        print(f"{player.name} has killed troll and found {prize} gold coins. "
              f"Now {player.name} has {player.money} gold coins and {player.life}/100 hit points left.")
        print(f"{player.name} feeling strong walks back towards river bank.")
        player.quest = 2
        print(
            f"Exhausted {player.name} leaves the cave. It's time to go back to the city to get reward from the order, isn't it?")
        river_direction(player)


def river_cave_02(player):
    print("Deeper in the cave you can see bulky figure of troll.")
    print("Indeed as the scribe said it isn't too big.")
    decision = input(f"{player.name} do you want to attack troll? You have {player.life} hit points. (attack/flee) ")
    if decision == "flee":
        print(f"{player.name} cowardly tries to flee, but troll notices it. He charges at you with fury! You have no time to prepare for fight.")
        river_troll_fight1(player)
    elif decision == "attack":
        if player.life <= 50:
            player.life = 70
            print(f"{player.name} focusing your powers you heal yourself. It's some kind of magic, maagic, maaaagic!")
        player.weapon += 1
        print(f"{player.name} decides to attack. {player.name} notices ring of power boosting his attack to {player.weapon}"
              f"With {player.life}/100 hit points you charge at the troll!")
        river_troll_fight2(player)


def river_cave_01(player):
    print(f"The entrance is really dark but behind the corner {player.name} finds primitive fire pit.")
    cave01_decision = input("Next to it sleeps wolf. Do you want to sneak by it or attack it? (sneak/attack) ")
    if cave01_decision == "sneak":
        if dice.roll_dice() >= 4:
            print(f"{player.name} sneaks by on tip toes.")
            river_cave_02(player)
        elif dice.roll_dice() < 4:
            print(f"Oh no! Clumsy {player.name} stomped on little twig and the wolf woke up. You need to fight for your life!")
            cave_wolf_encounter(player)
    elif cave01_decision == "attack":
        print(f"{player.name} grabs weapon and charges towards wolf!")
        cave_wolf_encounter(player)
    else:
        print("Please input command highlighted in the brackets.")
        river_cave_01(player)


def river_direction(player):
    decision = input("You are near the river bank. You can go north or east. Or travel somewhere else. (north/east/travel) ").lower()
    if decision == "north":
        print("You found cave entrance. You can't see too far inside.")
        if player.quest == 1:
            river_cave_01(player)
        elif player.quest == 0:
            print("You hear roar coming from dark cave. You don't feel like going inside!")
            river_direction(player)
        elif player.quest == 2:
            print("You have already dealt with troll living in this cave. No need to go there again.")
            river_direction(player)
        else:
            print("Please input 'north' or 'east'.")
            river_direction(player)
    elif decision == "east":
        print("On the small green grassland. You see small birds called Scavengers running around.")
        encounter_choice = input(f"{player.name} do you want to attack scavenger? Remember you have {player.life} hit points, "
                                 f"{player.weapon} attack points. (attack/back) ")
        if encounter_choice == "attack":
            print("You jump on the one of the scavengers.")
            opponent_life = 3
            while player.life > 0 and opponent_life > 0:
                if moving.encounter(player) == "Player win":
                    opponent_life -= player.weapon
                    print(
                        f"{player.name} hits Scavenger for {player.weapon} points! Scavenger has {opponent_life} hit points left.")
                elif moving.encounter(player) == "Opponent win":
                    player.life -= 10
                    print(f"{player.name} takes hit for 10 points. You have {player.life} hit points left.")
                else:
                    print(moving.encounter(player))
            if player.life == 0:
                print("Oh no, you are dead! X_X")
            elif opponent_life <= 0:
                prize = dice.roll_dice() * 10
                player.money += prize
                print(f"{player.name} has killed Scavenger and found {prize} gold coins. "
                      f"Now {player.name} has {player.money} gold coins and {player.life}/100 hit points left.")
                print(f"{player.name} feeling strong walks back towards river bank.")
                river_direction(player)
        elif encounter_choice == "back":
            print("You quiletly move back.")
            river_direction(player)
        else:
            print("Please input text according to the bracketed words.")
            river_direction(player)
    elif decision == "stats":
        commands.my_stats(player)
        river_direction(player)
    elif decision == "travel":
        to_travel = moving.where_to_go_river()
        if to_travel == "city":
            city.city_direction(player)
        elif to_travel == "stay":
            river_direction(player)
    else:
        commands.typo()
        river_direction(player)


def river_arrival(player):
    print(f"{player.name} arrived at the river bank.")
    print(gascii.river_view())
    river_direction(player)
