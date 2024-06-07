# #Data Types
#
# #String
#
# print("Hello"[4])
#
# #Integer
#
# print(111_111_111 + 222_222_222) # the _ is just to picture the number more clearly
#
# #Float
#
# 3.14159
#
# #Boolean
#
# True
# False
#
# # num_char = len(input("Your name ?"))
# # print(type(num_char))
# # str(num_char)
# # print(num_char)
# # print("Name has " + str(num_char) + " characters")
#
# 2 + 2
# 7 - 2
# 3 * 2
# 6 / 2
# print(2 ** 3)
#
# # How to round numbers
#
# print(round(8/3, 2)) #specifies the number of decimals
# print(type(8 // 3)) #specifies the type as an int
#
# score = 0
#
# score += 1
#
# height = 1.65
#
# #f-String
#
# print(f"your score is {score}, your height is {height}")

#Day 2 Project

print("Welcome to the tip calculator")
total_bill = input("What was the total bill?")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
num_people = input("How many people to split the bill? ")
bill = float(total_bill)/float(num_people) * (1 + (float(tip)/100))
print(f"Each person should pay: ${'%.2f' % bill}")

# To get 2 decimals even displaying 0, you need '%.2f % var'