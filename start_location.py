import dice
import gascii
import commands


def starting_path(player):
    print(gascii.start_loc_view())
    print("You wake up in the forest. It isn't dense. Small sign nearby shows three routes:\n"
          "'city', 'river' and 'mines'. However under is another sign with information that mines are closed.")
    choose = input("Where ya go? Or maybe do you wanna look around? (city/river/look): ").lower()
    if choose == 'city':
        return 'city'
    elif choose == 'river':
        return 'river'
    elif choose == 'stats':
        commands.my_stats(player)
        starting_path(player)
    elif choose == 'look':
        print("You look around. Notice small hut. Inside you meet weird gobling wearing medical smock. He wants to play a game.")
        print("""
               ,      ,
              /(.-""-.)\ 
          |\  \/      \/  /|
          | \ / =.  .= \ / |
          \( \   o\/o   / )/ 
           \_, '-/  \-' ,_/
             /   \__/   \ 
             \ \__/\__/ / 
           ___\ \|--|/ /___
         /`    \      /    `\ 
        /       '----'       \ \n       
        """)
        print("Goblin: Oh interesting creature stumbled by my study. Tell you what bud! Wanna get easy money?")
        print(f"{player.name}: Free money! Yaaay!")
        print("Goblin: Hold ya horses pal. If you wanna this money ya have to play dice with me. If ya win ya get 50 gold coins, if ya lose I'll take ya kidney. And after wards you will go to city.")
        goblin_choice = input(f"Goblin: So will you play with me {player.name}?\nThis time you can't use 'stats' to check what ya got. (yes/no) ")
        if goblin_choice == "yes" or goblin_choice == "y":
            goblin_roll = dice.roll_dice()
            player_roll = dice.roll_dice()
            if goblin_roll > player_roll:
                print(f"Oh you loose {player.name}. I'm taking your kidney then!")
                print("""
                 ______________________________ ______________________
                |                              | (_)     (_)    (_)   \ 
                |                              |  __________________   }
                |..........................____|_(                  )_/              
                """)
                player.life = 50
                return "city"
            elif goblin_roll < player_roll:
                print(f"Damn you {player.name}. You win this time, here's your money!")
                print(gascii.moneyz())
                player.money = 100
                return "city"
            else:
                print("Draw. What a shame. I'll take some of your hairs and have some money")
                print(gascii.moneyz())
                player.money = 60
                player.life = 90
                return "city"
        else:
            print("I see you are a coward! Scared of little, weak goblin?")
            print("That hits your morale, but you proceed to the city scared of green psycho")
            player.life -= 10
            return "city"
    else:
        commands.typo()
        starting_path(player)
