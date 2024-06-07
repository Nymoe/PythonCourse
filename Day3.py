#lower() turns a string into complete lowercase characters
#count() allows you to count the number of times an element is in an array

#Day 3 Project

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
/______/______/______/______/______/______/______/______/______/______/[#Nymoe]
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\" \n")
choice1 = choice1.lower()
if choice1 == "right":
    print("Game Over")
else:
    print("You arrived at a lake...")
    choice2 = input("Would you like to swim or wait for a boat? Type \"swim\" or \"wait\" \n")
    choice2 = choice2.lower()
    if choice2 == "swim":
        print("Game Over")
    else:
        print("You arrive at a door and have to choose between 3 doors: Yellow, Blue or Red")
        choice3 = input("Which door would you like to enter? Type \"yellow\" or \"blue\" or \"red\" \n")
        choice3 = choice3.lower()
        if choice3 == "red" or choice3 == "blue":
            print("Game Over")
        else:
            print("You Win !")