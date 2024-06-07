# #Find the number of cans of paint required to do the task depending on the surface
# def paint_calc(height, width, cover):
#   cans = height * width / cover
#   if cans % cover != 0:
#     cans = round(cans) + 1
#   print(f"You'll need {cans} cans of paint.")
#
# test_h = 2 # Height of wall (m)
# test_w = 11 # Width of wall (m)
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)
#
# # Find if the number in the argument is a prime number
# def prime_checker(number):
#   prime = True
#   for i in range(2, number):
#     if number % i == 0:
#       prime = False
#   if prime:
#     print("It's a prime number.")
#   if not prime:
#     print("It's not a prime number.")
#
# n = int(input())  # Check this number
# prime_checker(number=n)

# Project Day 8

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
#Encrypt
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

#Decrypt
#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
#TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
  #e.g.
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.
# Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
def encrypt(text, shift):
  encoded_msg = ""
  for i in text:
    position = alphabet.index(i)
    if position + shift > len(alphabet) - 1:
      position = position + shift - len(alphabet) - 1
    else:
      position = position + shift
    encoded_msg += alphabet[position]
  print(encoded_msg)

def decrypt(text,shift):
  plain_msg = ""
  for i in text:
    position = alphabet.index(i)
    if position - shift < 0:
      position = position - shift + len(alphabet) - 1
    else:
      position = position - shift
    plain_msg += alphabet[position]
  print(plain_msg)




def caesar(text, shift, direction):
  if direction == "encode":
    encrypt(text, shift)
  else:
    decrypt(text, shift)
