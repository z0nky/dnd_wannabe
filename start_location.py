import dice


def starting_path(player):
    print("starting location description")
    choose = input("Where ya go? Or maybe do you wanna look around? (city/river/look): ")
    if choose == 'city':
        return 'city'
    elif choose == 'river':
        return 'river'
    elif choose == 'look':
        print("You look around. Notice small hut. Inside you meet weird gobling wearing medical smock. He wants to play a game.")
        print("Dialogue 1, blah blah regardless you will have to promise me to go to the city.")
        goblin_choice = input(f"So will you play with me {player.name}? (yes/no)")
        if goblin_choice == "yes" or goblin_choice == "y":
            goblin_roll = dice.roll_dice()
            player_roll = dice.roll_dice()
            if goblin_roll > player_roll:
                print(f"Oh you loose {player.name}. I'm taking your kidney then!")
                player.life = 50
                return "city"
            elif goblin_roll < player_roll:
                print(f"Damn you {player.name}. You win this time, here's your money!")
                player.money = 100
                return "city"
            else:
                print("Draw. What a shame. I'll take some of your hairs and have some money")
                player.money = 60
                player.life = 90
                return "city"
        else:
            print("I see you are a coward!")
            print("THat hits your morale, but you proceed to the city scared of green psycho")
            player.life -= 10
            return "city"
    else:
        print('Please input one of presented options in bracket.')
        starting_path(player)

