import random
import commands


def name_choice(user_choice_gender, race):
    usa_choi = input("Do you want to auto generate name (lazy option!)? (y/n): ").lower()
    global choosen_name
    if usa_choi == "y" or usa_choi == "yes":
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
    elif usa_choi == "n" or usa_choi == "no":
        choosen_name = input("So please enter your name. Be aware that we do not care if you:"
                             "\n - write some nonsense like '5w33t ki113r'"
                             "\n - about you willing to change your mind after entering the name"
                             "\n - because if you are not lazy you can do it properly!"
                             "\n - we only allow names with maximum length of 50 symbols!"
                             "\n - if it is longer than 50 symbols we will punish you by giving you mean name!"
                             "\n So yeah. Please inter your name: ").capitalize()
        if len(choosen_name) > 50:
            choosen_name = "Dummy"
            return choosen_name
        return choosen_name
    else:
        commands.typo()
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
        commands.typo()
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
        commands.typo()
        character_creator()


def character_creator():
    print(" Who you want to be ?")
    print(" Select an option:")
    print(" 1 - Female ♀")
    print(" 2 - Male ♂")
    user_choice_gender = input("Choose the gender. Input 1 or 2: ")
    select_character(user_choice_gender)
    return user_choice_gender


def start_creator():
    print("Now you will create your character.")
    character_creator()


# hu_m, or_m, el_m, hu_f, or_f, el_f
name_pool = [["Zygfryd", "Gerwazy", "Zawisza"],
["Wrukag", "Zargulg", "Sunuguk"],
["Methild", "Almon", "Elre"],
["Anna", "Rita", "Yennefer"],
["Grat", "Yazgash", "Burzob"],
["Caeda", "Shenarah", "Ayda"]]

