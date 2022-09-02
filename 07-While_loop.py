"""python --  while loop"""

word = "python"

i = 0               # this loop is not validated if we do not put a value of i
while i < 10:  
    print(word)     # we see that i < 10 so it will print the word several times

    i+=1      # we started with 0 so when it prints the word for the first time it will add 1 to the value (i=0)
              # and it will re-add and print up to the value (i=10) and like that the loop stops

#----------------------------------------------------------------------------

"""Nested - while loop"""

i = 0
while i <5:
    print("python")  # the loop takes the first value of (range) and it puts the value in (i) and it prints(a)
    i+=1

    j=0
    while j<3:       # after it executes the second loop
        print("java")
        j+=1

# after it returns to the first loop to take the second value of (i) and it re executes
#  the second loop then it does the same until the last value of the first loop.

# output = python
# java
# java
# java
# python
# java
# java
# java
# python
# java
# .


# or    we can put i+=1 at the end of the  second loop (here).

i = 0
while i <5:
    print("python")  # the loop takes the first value of (range) and it puts the value in (i) and it prints(a)
    
    j=0
    while j<3:       # after it executes the second loop
        print("java")
        j+=1
    i+=1    #(here)



i = 1
while i <= 4 :
    j = 0
    while  j <= 3 :
        k = 0
        while  k <= 5 :
            print(i*j*k, end=" ")
            k += 1
        print()
        j += 1
    print()
    i += 1

# output 
# 0 0 0 0 0 0
# 0 1 2 3 4 5
# 0 2 4 6 8 10
# 0 3 6 9 12 15
 
# 0 0 0 0 0 0
# 0 2 4 6 8 10
# 0 4 8 12 16 20
# 0 6 12 18 24 30
 
# 0 0 0 0 0 0
# 0 3 6 9 12 15
# 0 6 12 18 24 30
# 0 9 18 27 36 45
 
# 0 0 0 0 0 0
# 0 4 8 12 16 20
# 0 8 16 24 32 40
# 0 12 24 36 48 60
#------------------------------------------------------------------
# Prints all letters except 'e' and 's'
i = 0
a = 'geeksforgeeks'
  
while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue
          
    print('Current Letter :', a[i])
    i += 1

#-------------------------------------------------------
x = 'spam'
while x:                # While x is not empty
    print(x, end=' ')   # (end) pour mettre les resultat sur la meme ligne
    x = x[1:]           # Strip first character off x

x = 'spam'
while x:                # While x is not empty
    print(x)
    x = x[1:]           # Strip first character off x

#-------------------------------------------------------
a=0
b=10
# ou on peut mettre  a=0; b=10
while a < b:            # One way to code counter loops
    print(a, end=' ')
    a += 1               # Or, a = a + 1
#-------------------------------------------------------
x = 10
while x:
    x = x - 1           # Or, x -= 1
    if x % 2 != 0:      # the first value will be 9 because (x=10) and x = x-1 then 9% 2!= 0 it will continue without printing
        continue        # Odd? -- skip print
    print(x, end=' ')
#-------------------------------------------------------
x = 10
while x:
    x -=1
    if x % 2 == 0:      # Even? -- print
        print(x, end=' ')
#-------------------------------------------------------
while True:
    name = input('Enter name:')
    if name == 'stop':
        break
    age = input('Enter age: ')
    print('Hello', name, '=>', int(age) ** 2)
    break



#-------------------------------------------------------
n = 5
while n > 0:
    n = n - 1
    if n == 2:
        break
    print(n)
else:
    print("Loop is finished")


#-------------------------------------------------------
n = 5
while n > 0:
    n = n - 1
    if n == 2:
        continue
    print(n)
else:
    print("Loop is finished")

#-------------------------------------------------------
# Instantiate a variable i with the value 1.
# Using a while loop, display the first 10 natural numbers.

i = 1

# Tant que i est inférieur à 10
while i <= 10:
    # On affiche i
    print(i)
    
    # On incrémente i de 1
    i += 1
results = [9.81, 9.89, 9.91, 9.93, 9.94, 9.95, 9.96, 9.97, 9.98, 10.03, 10.04, 10.05, 10.06, 10.08, 10.11, 10.23]

# Insérez votre code ici
nombre_athletes = 0

i = 0

# We have a list containing the times achieved by athletes during a 100m race.
# The results are sorted in ascending order.

# Using a while loop, determine how many athletes clocked less than 10s.

while i < len(results):
    
    if results[i] < 10:
     
        nombre_athletes += 1
        
    i += 1

print(f"il y a {nombre_athletes} athlètes ont réalisé un temps inférieur à 10s.")

# ---------------------------------------------------------------------------
# for i in range(1,11):
#     print(f"i is now {i}")

i = 0
while i < 10:
    print(f"i is now {i}")
    i +=1

print("-"*50)

i = 0
while True:
    print(f"i is now {i}")
    i +=1
    if i == 100:
        break
print("-"*50)
# -----------------------------------------------------------





available_exits  = ["north","south","west","east"]

chosen_exit = ""

while chosen_exit not in available_exits:
    chosen_exit= input("choose a diriction please: ")

print("good job you can be free")

print("-"*50)

# ----------------------------------------------
import random

highest=10
answer = random.randint(1,highest)

print(f"Please guess a number between 1 and {highest} and to quit the game please put the number 0 :")

guess=0
while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    else:
        if guess == answer:
            print("well done")
        elif guess > answer:
            print("please guess lower")
        else:
            print("please guess higher")

# ---------------------------------------------------------------------------
"""while-else loop"""  
i = 0
while i < 4:
    i += 1
    print(i)
else:  # Executed because no break in for
    print("No Break\n")
  
i = 0
while i < 4:
    i += 1
    print(i)
    break
else:  # Not executed as there is a break
    print("No Break")
# ---------------------------------------------------------------------------
# This loop will only run 1 time
hungry = True
while hungry:
  print("Time to eat!")
  hungry = False

# This loop will run 5 times
i = 1
while i < 6:
  print(i)
  i = i + 1
# ---------------------------------------------------------------------------
# while loop - if/else statements
counter = 1
while (counter < 5):
    count = counter
    if count < 2:
        counter = counter + 1
    else:
        print('Less than 2')
    if count > 4:
        counter = counter + 1
    else:
        print('Greater than 4')
    counter = counter + 1 

counter = 1
while (counter < 5):
    if counter < 2:
        print('Less than 2')
    elif counter > 4:
        print('Greater than 4')
    else:
        print('Something else') # You can use 'pass' if you don't want to print anything here
    counter += 1

x = 1
while x<=5:
    print(x)
    if x == 3:
        x = x + 1
        continue
    else:
        print(x)
        x = x + 1

# output

# 1
# 1
# 2
# 2
# 3 
# 4
# 4
# 5
# 5
# -----------------------------------------------------------

available_exits = ["north", "south", "west", "east"]

chosen_exit = ""

while chosen_exit not in available_exits:
    chosen_exit = input("choose a diriction please: ")
    # the loop will still runing if we didn't use the if condition
    if chosen_exit.casefold() == "quit":
        print("Game Over")
        break       # we will be break if we input(quit) 

else:     # this else is utside the loop, this condition should never be reached if the if condition was executed
    print("good job you can be free")    # it will print this after the end of the loop
                          
# ----------------------------------------------------------------
available_parts = ["computer","monitor","mouse","keyboard"]

valid_choice=[str(i)for i in range (1,len(available_parts)+1)]
print(valid_choice)
current_choice = "-"
computer_parts = []

while current_choice != "0":
    if current_choice in valid_choice:
        # print(f"adding {current_choice}")
        index = int(current_choice) -1     # -1 because we put a +1 in valid choice to start the index from 1 not from 0
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            print(f"removing {current_choice}")
            computer_parts.remove((chosen_part))
        else:
            print(f"adding {current_choice}")
            computer_parts.append((chosen_part))
        print(f"your list contains: {computer_parts}")

    
    elif len(computer_parts) == len(available_parts):
        break
    
    else:
        print("please add option from the list below:")
        for number, part in enumerate(available_parts):
            print(f"{number + 1} {part}")
    current_choice = input()
print(computer_parts)
print(computer_parts.index("computer"))
