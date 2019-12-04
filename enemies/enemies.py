import dice


class Monsters():
    def __init__(self):
        pass

    def __repr__(self):
        return f'{self.__class__.__name__} {self.life} hp.'

    def attack(self):
        return dice.roll_dice() + self.difficulty

    def attack_disadvantage(self):
        return dice.roll_dice_2k12() + self.difficulty


class Scavenger(Monsters):
    def __init__(self):
        super().__init__()
        self.life = 30
        self.difficulty = 1


class Wolf(Monsters):
    def __init__(self):
        super().__init__()
        self.life = 40
        self.difficulty = 2


class Troll(Monsters):
    def __init__(self):
        super().__init__()
        self.life = 60
        self.difficulty = 4


scav = Scavenger()
t = Troll()
print(scav)
print(scav.attack())
print(t.attack())
print(t.attack_disadvantage())