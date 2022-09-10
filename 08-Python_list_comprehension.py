"""List comprehension"""

# # Python list comprehensions provide a concise way for creating lists. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses: [EXPRESSION for ITEM in LIST <if CONDITIONAL>].

# # The expressions can be anything - any kind of object can go into a list.

# # A list comprehension always returns a list.

# # List comprehension for the squares of all even numbers between 0 and 9
# result = [x**2 for x in range(10) if x % 2 == 0]

# print(result)
# # [0, 4, 16, 36, 64]

# List comprehension is an extremely interesting concept with Python,
# and which is part of the central objective of simplifying codes and gaining productivity.

# By using the syntax of for loops, it allows to define in a very compact and elegant way a list of values.

# We want to store the first 10 squared integers in a list. To do this, we can create an empty list and use a for loop as before:

# my_list = []
# for i in range(10):
#     my_list.append(i**2)
# But Python allows us to reduce this writing, thanks to the list comprehension:

# my_list = [i**2 for i in range(10)]
# These two methods are strictly equivalent.

# So, for one of the previous exercises where we wanted to increase all scores by 4 points, we could have done:

# good_marks = [mark + 4 for mark in bad_marks]
# Using the list comprehension method:

# (a) Store in a list named powers_three the first 10 powers of 3.
# (b) A list list_numbers is given to you. Create a new list double_list containing the double of each of its elements.
# (c) From list_numbers, create a list list_evens which for each number in list_numbers indicates "even"
# if the number is even, and "odd" otherwise. Parity can be tested using the modulo % operator.
# We recall the syntax of the conditional assignment:

# # A student repeats if his average is less than 10
# redouble = True if average < 10 else False

liste_nombres = [10, 12, 7, 3, 26, 2, 19]

puissances_trois = [3**k for k in range(10)]

liste_doubles = [nombre * 2 for nombre in liste_nombres]

liste_pairs = ["pair" if nombre % 2 == 0 else "impair" for nombre in liste_nombres]

print(puissances_trois)
print(liste_doubles)
print(liste_pairs)

# -------------------------------------------------------------------------
lst = []
for i in range(100):
    lst.append(i / 100)

print(lst)
print()

f = [i / 100 for i in range(100)]
print(f)
