# import dice
# import moving
#
#
# class Player:
#     def __init__(self, name):
#         self.name = name
#         self.life = 100
#         self.weapon = 1
#         self.money = 50
#         self.quest = 0
#
#     def __str__(self):
#         return f"{self.name} has {self.life} % life and {self.weapon} current weapon and {self.money} gold coins in pocket."
#
# player = Player("UN")
#
# opponent_life = 5
# while player.life > 0 and opponent_life > 0:
#     if moving.encounter_disadvantage(player) == "Player win":
#         opponent_life -= player.weapon
#         print(f"{player.name} hits Scavenger for {player.weapon} points! Scavenger has {opponent_life} hit points left.")
#     elif moving.encounter_disadvantage(player) == "Opponent win":
#         player.life -= 10
#         print(f"{player.name} takes hit for 10 points. You have {player.life} hit points left.")
#     else:
#         print(moving.encounter_disadvantage(player))
# if player.life == 0:
#     print("Oh no, you are dead! X_X")
# elif opponent_life <= 0:
#     prize = dice.roll_dice() * 10
#     player.money += prize
#     print(f"{player.name} has killed Scavenger and found {prize} gold coins. "
#           f"Now {player.name} has {player.money} gold coins and {player.life}/100 hit points left.")

print(
"""
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
/       '----'       \ 
                                 """)