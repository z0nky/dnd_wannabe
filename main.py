import character
import start_location
import moving
import city


class Player:
    def __init__(self, name):
        self.name = name
        self.life = 100
        self.weapon = 100
        self.money = 50
        self.quest = 0

    def __str__(self):
        return f"{self.name} has {self.life} % life and {self.weapon} current weapon and {self.money} gold coins in pocket."


def main_menu():
    return ('New Game - 1'
            '\nContinue Last Game - 2'
            '\nExit - 3')


def main():
    print(('MAIN MENU').center(20, "*"))
    print(main_menu())
    go_to = input('Insert menu number positon (1-3): ')
    if go_to == '1':
        start_game()
    elif go_to == '2':
        print("This feature is unavailable. Please pay 100€ for incoming DLC so I will input if asap!")
        main()
    elif go_to == '3':
        exit_the_program()
    else:
        print('Please enter number from range 1-3.')
        main()


def exit_the_program():
    print('*' * 5, '\nThanks for playing, come again soon!')


def start_game():
    character.start_creator()
    player = Player(character.choosen_name)
    print(player)
    location = start_location.starting_path(player)
    if location == "city":
        print(f"{player.name} will go to the city.")
        city.enter_the_city(player)
    elif location == "river":
        print(f"{player.name} will go to the river.")
    print(player)
    city.city_direction(player)


if __name__ == "__main__":
    main()
