import random

from numpy.random import randint

#randint(a,b) can generate a random int from a to b

#random() can generate a float from 0 and 1 (1 not included)

# list = ["1", "2"]
# list2 = [1, 2]
# list3 = [list, list2]

#print(list3)

#list[-1] would be the last item in the array

#print(list[-2])

#list.append() or list.extend(iterable) or list.insert(i,x) or list.remove(x) or list.pop([i])/list.pop() (last item if not specified)

#Auditorium : Lesson 15

# line1 = ["","",""]
# line2 = ["","",""]
# line3 = ["","",""]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input() # Where do you want to put the treasure?
# # 🚨 Don't change the code above 👆
# # Write your code below this row 👇
# #Preferable to use the index metho letter.index('A') to compare A to the letter input
# if position[0] == "A":
#   if position[1] == "1":
#     map[0][0] = 'X'
#   elif position[1] == "2":
#     map[1][0] = "X"
#   elif position[1] == "3":
#     map[2][0] = 'X'
# elif position[0] == "B":
#   if position[1] == "1":
#     map[0][1] = 'X'
#   if position[1] == "2":
#     map[1][1] = 'X'
#   if position[1] == "3":
#     map[2][1] = "X"
# elif position[0] == "C":
#   if position[1] == "1":
#       map[0][2] = 'X'
#   elif position[1] == "2":
#       map[1][2] = 'X'
#   elif position[1] == "3":
#       map[2][2] = 'X'
#
# # Write your code above this row 👆
# # 🚨 Don't change the code below 👇
# print(f"{line1}\n{line2}\n{line3}")

#Project Day 4

rock = "rock"
paper = "paper"
scissors = "scissors"

choices = [rock, paper, scissors]

computer_choice = choices[randint(0,2)]
player_choice = choices[int(input("What is your choice? Type 1 for rock, 2 for paper, 3 for scissors\n"))]
print(f"You chose {player_choice} and the computer chose {computer_choice}")
if player_choice == choices[0]:
    if computer_choice == choices[0]:
        print("It's a tie !")
    elif computer_choice == choices[1]:
        print("You lost!")
    elif computer_choice == choices[2]:
        print("You win!")
elif player_choice == choices[1]:
    if computer_choice == choices[0]:
        print("You win!")
    elif computer_choice == choices[1]:
        print("It's a tie !")
    elif computer_choice == choices[2]:
        print("You lost!")
elif player_choice == choices[2]:
    if computer_choice == choices[0]:
        print("You lost!")
    elif computer_choice == choices[1]:
        print("You win!")
    elif computer_choice == choices[2]:
        print("It's a tie !")
