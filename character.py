import random


def name_choice(user_choice_gender, race):
    usa_choi = input("Do you want to auto generate name (lazy option!)? (y/n): ")
    global choosen_name
    if usa_choi == "y":
        if user_choice_gender == "1":
            if race == "Human":
                choosen_name = random.choice(name_pool[3])
                return choosen_name
            elif race == "Orc":
                choosen_name = random.choice(name_pool[4])
                return choosen_name
            else:
                choosen_name = random.choice(name_pool[5])
                return choosen_name
        if user_choice_gender == "0":
            if race == "Human":
                choosen_name = random.choice(name_pool[0])
                return choosen_name
            elif race == "Orc":
                choosen_name = random.choice(name_pool[1])
                return choosen_name
            else:
                choosen_name = random.choice(name_pool[2])
                return choosen_name
    elif usa_choi == "n":
        choosen_name = input("So please enter your name: ")
        return choosen_name
    else:
        print("Please writh 'y' or 'n'!")
        name_choice(user_choice_gender, race)


def race_choice():
    print("What is your race please select from option")
    print(" 1 - If you are an Orc")
    print(" 2 - If you are an Human")
    print(" 3 - If you are an Elf")
    select = input('')
    if select == "1":
        race = "Orc"
        return race
    elif select == "2":
        race = "Human"
        return race
    elif select == "3":
        race = "Elf"
        return race
    else:
        print('dupa')
        race_choice()


def select_character(select):
    if select == '1':
        gender = "1"
        select = race_choice()
        name_choice(gender, select)
    elif select == '2':
        gender = "0"
        select = race_choice()
        name_choice(gender, select)
    else:
        print("You didn't input 1 or 2, please do so!")
        character_creator()


def character_creator():
    print(" Who you want to be ?")
    print(" Select an option:")
    print(" 1 - Women")
    print(" 2 - Man")
    user_choice_gender = input("Choose the gender. Input 1 or 2: ")
    select_character(user_choice_gender)
    return user_choice_gender


def start_creator():
    print( "This is the Game ")
    character_creator()


# hu_m, or_m, el_m, hu_f, or_f, el_f
name_pool = [["Zygfryd", "Gerwazy", "Zawisza"],
["Wrukag", "Zargulg", "Sunuguk"],
["Methild", "Almon", "Elre"],
["Anna", "Rita", "Yennefer"],
["Grat", "Yazgash", "Burzob"],
["Caeda", "Shenarah", "Ayda"]]


# class Player:
#     def __init__(self, name, life, weapon, money):
#         self.name = name
#         self.life = life
#         self.weapon = weapon
#         self.money = money
#
#     # dodawanie (ujemne) money
#     def wallet(self):
#         pass
#
#     # dodawanie weapon
#     def buy(self):
#         pass
#
#     # odejmowanie hp
#     def damage(self):
#         pass
#
#     # dodawanie hp
#     def heal(self):
#         pass
#
#
