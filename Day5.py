# #Syntax of a for loop
#
# list = [0,1,2,3,4,5,6,7,8,9]
#
# for i in list:
#     print(f"List is {i}")
#
# for i in range(0,10):
#     print(f"Range is {i}")

#Project Day5

#Password Generator Project
import numpy as np
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
size_letters = len(letters)
size_numbers = len(numbers)
size_symbols = len(symbols)

size_password = nr_letters + nr_symbols + nr_numbers
password = ""
for i in range(0,size_password):
    if i < nr_letters:
        password += letters[random.randint(0,size_letters-1)]
    elif i < nr_letters + nr_symbols:
        password += (symbols[random.randint(0, size_symbols-1)])
    elif i < size_password:
        password += (numbers[random.randint(0, size_numbers-1)])
print(password)

#OR

password2 = ""
for i in range(0,size_password):
    if i < nr_letters:
        password2 += random.choice(letters)
    elif i < nr_letters + nr_symbols:
        password2 += random.choice(symbols)
    elif i < size_password:
        password2 += random.choice(numbers)
print(password2)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#Can use the function random.shuffle(list)

random_password = ""
list_index = []
while len(random_password) < size_password:
    index = random.randint(0,size_password - 1)
    if index not in list_index:
        list_index.append(index)
        random_password += password2[index]
print(f"This is a random order for the password {random_password}")