"""if_else conditions""" 

import math
import os
import random
import re
import sys

# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range 6 of  to 20 , print Weird
# If  is even and greater than 20, print Not Weird

N = int(input("enter a number"))

if N % 2 != 0:                  # odd number
    print("Weird")
else:
    # if N >= 2 and N <= 5  :     # the number is in range (2,5)
    #     print("Not Weird")
    # or
    if N in range (2,5):
        print("Not Weird")
    elif N >= 6 and N <= 20:
        print("Weird")
    elif N % 2 == 0 and  N > 20:
        print("Not Weird")


# -----------------------------------------------------------------------------------------------------
age = int(input("enter your age"))

if age >=20 and age <=30:
    print("you are young")

 # -----------------------------------------------------------------------------------------------------   
x = 10
y = 7


if x < y :
    print (x)      # we have x is > of y then it will print nothing


if x>y:
    print(x)       # we have x is > of y then it will print the amount of x ( 10 )
    z = x+y        # this operation will not be executed if the first condition was not validated
    print(z)       # it gives the result of z because the first condition was validated (result = 17)


if x<y:
    print(x)       # we have x is > of y then it will print nothing
    z = x+y        # this operation will not be executed if the first condition was not validated
    print(z)       # the first condition was not validated it will print nothing
else:
    print(y)      # we use (else) because the first condition was not validated (result = 7 )

if x<y:
    print(x)       # we have x is > of y then it will print nothing
    z = x+y        # this operation will not be executed if the first condition was not validated
    print(z)       # the first condition was not validated it will print nothing

elif y <x:          # we use (elif) to have a second condition before using (else)
    print(x)       # y < x then the condition is validated ( result = x --> = 10 )

else:
    print(y)       # one of two conditions is validated then it will print nothing

# # -----------------------------------------------------------------------------------------------

utilisateur = "admin"
if utilisateur == "admin":
    print("Accès autorisé 1!")      # Accès autorisé 1!
elif utilisateur == "root":
    print("Accès autorisé !")       
else:
    print("Accès refusé...")


utilisateur = "root"
if utilisateur == "admin":
    print("Accès autorisé !")       
elif utilisateur == "root":
    print("Accès autorisé 2!")      # Accès autorisé 2!
else:
    print("Accès refusé...")

utilisateur = "spam"
if utilisateur == "admin":
    print("Accès autorisé !")       
elif utilisateur == "root":
    print("Accès autorisé 2!")      
else:
    print("Accès refusé...")        # Accès refusé...



# # ----------------------------------------------------------------------------------------------

day = 1

if (day == 1):
    print("saturday")     # saturday
elif (day == 2):
    print("sunday")
elif (day == 2):
    print("sunday")
elif (day == 3):
    print("monday")
elif (day == 4):
    print("tuesday")

else:
    print("None")

# -----------------------------------------------------------------------------------------------
"""Nested-if"""


age = 30

name = "ali"

if (age <= 20):                  # we look to the first condition if it's not respected so nothing will be printed
    if (name == "ali"):
        print("you are young")   # this condition will be validated if the two if are validated(age= 20, name= ali)
    else:
        print("None")            # the age not the the same then nothing will be printed

elif (age <= 30):
    if (name == "hasan"):
        print("you are not young") # this condition will be validated if the two if are validated(age= 30, name= hasan)
    else:
        print("None")              # if the age was 30 but the name was not the same then it will print (None)

else:
    print("you are old")           # if no condition was validated then it will apply ( else ) (you are old)



if (age <= 30):                  
    if (name == "ali"):
        print("you are young")   # you are young
    else:
        print("None")            

elif (age <= 30):
    if (name == "hasan"):
        print("you are not young") 
    else:
        print("None")             # None

else:
    print("you are old")         # if no condition was validated then it will apply ( else ) (you are old)


# -----------------------------------------------------------------------------------------------

d = {'Race': 'Maître du temps', 'Vaisseau': 'TARDIS', 'nom': 'Le Docteur', 'Origine': 'Gallifrey'}


# test the if condition with a dictionary
if d["nom"] == "Le Docteur":
    print("Sauvé ! c'est le docteur !")



if d["nom"] == "Le Docteur":
    print("Sauvé ! c'est le docteur !")
else:
    print("Perdu ! ce n'est pas le docteur !")


# -----------------------------------------------------------------------------------------------

name = input("Please enter your name: ")
age = int(input(f"How old are you {name}: "))

#or
age2= int(input("what's your date of birth {0}: ".format(name)))
print("your age is : {0} ".format(age))
print(f"your date of birth is : {age2}")

if age >= 18:
    print("you are old enough to vote")
else:
    print(f"you are young, please come back in {18-age}"+" years.")

if age < 18:
    print(f"you are young, please come back in {18-age}"+" years.")
else:
    print("you are old enough to vote")

# -----------------------------------------------------------------------------------------------
if age < 18:
    print(f"you are young, please come back in {18-age}"+" years.")
elif age == 90:
    print("stay at home you need to take a nap")
else:
    print("you are old enough to vote")
# -----------------------------------------------------------------------------------------------
age = int(input("How old are you?"))

if age >=16 and age <=65:
    print("Have a good day at work")

if 16<= age <=65:
    print("Have a good day at work")
else:
    print("Enjoy your life")

print("-"*50)

if age >16 or age <=65:
    print("Have a good day at work")
else:
    print("Enjoy your life")


print("-"*50)

if age in range(16,66):
    print("Have a good day at work")
else:
    print("Enjoy your life")

    
# -----------------------------------------------------------------------------------------------
day = "Monday"
temprature = 30
raining = True

if day == "Monday" and temprature > 27 and not raining:
    print("it's a good day")
else:
    print("Stay at home")

day = "saturday"

temprature = 30
raining = True

if day == "saturday" and temprature > 27 or not raining:
    print("it's a good day")
else:
    print("Stay at home")

day = "friday"

temprature = 25
raining = False

if day == "saturday" and temprature > 27 or not raining:
    print("it's a good day")
else:
    print("Stay at home")


name = input("Please enter your name :")
if name != "":
    print("Hello {}".format(name))
else:
    print("Are you the man with no name")

print("-"*50)
# -----------------------------------------------------------------------------------------------

parrot = "Norwegian Blue"
letter = input("Enter a character")

if letter in parrot:
    print("{} is in {}".format(letter,parrot))

print("-"*50)

name = input("Please enter your name :")
age = int(input("Please enter your age :"))

if 18 <= age <31:
    print("Hello {0}".format(name))

# -----------------------------------------------------------------------------------------------
parrot = "Norwegian Blue"
# python is a case sensitive so if we want to input a letter majescule ( R in norwegian is miniscule)
# so we need to use .lower() to transform what we input to lower case
letter = input("Enter a character").lower()  

if letter in parrot:
    print("{} is in {}".format(letter,parrot))
    # or print(f"{letter} is in {parrot}")
# -----------------------------------------------------------------------------------------------
parrot = "Norwegian Blue"
# python is a case sensitive so if we want to input a letter majescule ( R in norwegian is miniscule)
# so we need to use .casefold()  to transform what we input to lower case
letter = input("Enter a character").casefold()  

if letter in parrot:
    print("{} is in {}".format(letter,parrot))
    # or print(f"{letter} is in {parrot}")
# -----------------------------------------------------------------------------------------------
answer = 5

print("please guess the answer")
guess = int(input("enter a number between 1 and 10: "))

if guess != answer and guess > 10 or guess <=0  : # we use (and , or) if we have multi conditions.
    print("accepted numbers are between 1 and 10")
    if guess != answer:
        print("please enter another number")
        guess = int(input("guess a number "))
        if guess == answer:
            print("you guess it")

        elif guess > answer:
            print("please enter a lower number!!")  
            guess = int(input("guess a number "))
            if guess == answer:
                print("you guess it")
            else:
                print("try again") 

        elif guess < answer:
            print("please enter a higher number!!")
            guess = int(input("guess a number "))
            if guess == answer:
                print("you guess it")
            else:
                print("try again")


else:
    print("good job you guess it")

# -----------------------------------------------------------------------------------------------------

answer = 5

print("please guess the answer")
guess = int(input("enter a number between 1 and 10: "))

if guess != answer and guess < answer:
    print("please enter a higher number")
    guess = int(input("guess a number "))
    if guess == answer:
        print("you guess it")
    else:
        print("sorry you didn't guess it")
elif guess != answer and guess > answer:
    print("please enter a lower number")  
    guess = int(input("guess a number "))
    if guess == answer:
        print("you guess it")    
    else:
        print("sorry you didn't guess it")

else:
    print("good job you guess it")

# -----------------------------------------------------------------------------------------------------
age = int(input("enter your age"))

if age >=20 and age <=30:
    print("you are young")
# -----------------------------------------------------------------------------------------------------
name = input("enter your name: ")

if name:       # that is a boleean methode ( if name that is mean True)
    print(f"that's your name: {name} ")
else:
    print("you don't have a name!!!!")   # if we put nothing (False)
# -----------------------------------------------------------------------------------------------------
# guessing game

highest=10
answer = random.randint(1,highest)

print(f"Please guess a number between 1 and {highest} :")

guess=0
while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    else:
        if guess > answer:
            print("please guess lower")
        elif guess == answer:
            print("well done")
        else:
            print("please guess higher")
# -----------------------------------------------------------------------------------------
shopping_list = ["milk","egg","spam","water"]

item_to_found = "pasta"

found_at = None

if item_to_found in shopping_list:
    found_at = shopping_list.index(item_to_found)
    print(f"item found at the {found_at} position.")

if found_at is not None:
    print(f"item found at position {found_at}")
else:
    print(f"{item_to_found} not found ")

    