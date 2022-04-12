print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


First = input(
    "You're at a crossroad. Where do you want to go? Type 'left' or 'right'\n")
first = First.lower()
if first == "right":
  print("game over")
if first == "left":
  Second = input(
      "You have come to a lake. there is an island across from the lake. \ntype 'wait' to wait for a boat. type 'swim' to swim across\n")
second = Second.lower()
if second == "swim":
  print("You get attacked by one ulua Game Over")
if second == "wait":
  Last = input("A boat passes by and picks you up,\nyou arrive at the island unharmed\nat the island you see a house, there are three doors one red, one yellow, and one blue. which color door do you choose?\n")
last = Last.lower()
if last == "red":
  print("You enter a room full of fire. Game Over")
if last == "yellow":
  print("You walk through the door and a blackhole is on the otherside, you are never seen again")
if last == "blue":
  print("you walk through the door and there is a pile of gold and a tesla, congrats! you win.")
