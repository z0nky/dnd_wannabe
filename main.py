import character
import start_location
import river
import city
import commands
import gascii


class Player:
    def __init__(self, name):
        self.name = name
        self.life = 100
        self.weapon = 5
        self.money = 50
        self.quest = 0

    def __str__(self):
        return f"{self.name} has {self.life} % life and {self.weapon} current attack power and {self.money} gold coins in pocket."


def main_menu():
    print(gascii.asc_mainmenu().center(50))
    return ('New Game - 1'
            '\nContinue Last Game - 2'
            '\nExit - 3')


def main():
    print(main_menu())
    go_to = input('Insert menu number positon (1-3): ')
    if go_to == '1':
        start_game()
    elif go_to == '2':
        print("This feature will be added in paid DLC.")
        main()
    elif go_to == '3':
        exit_the_program()
    else:
        commands.typo()
        main()


def exit_the_program():
    print(gascii.exit())
    decide = input("Yes or no? ").lower()
    if decide == "yes" or decide == "y":
        print('*' * 5, '\nThanks for playing, come again soon!')
    elif decide == "no" or decide == "n":
        print("Oh I'm glad you are staying after all!")
        main()
    else:
        commands.typo()
        exit_the_program()


def start_game():
    character.start_creator()
    player = Player(character.choosen_name)
    commands.clean_up()
    commands.my_stats(player)
    print("From now on if you use command 'stats' you can check your stats. They will appear as shown above.")
    location = start_location.starting_path(player)
    if location == "city":
        print(f"{player.name} will go to the city.")
        if player.life > 0:
            city.enter_the_city(player)
            if player.quest == 666:
                print("")
                exit_the_program()
        else:
            commands.game_over(player)
    elif location == "river":
        print(f"{player.name} will go to the river.")
        river.river_arrival(player)


if __name__ == "__main__":
    main()
