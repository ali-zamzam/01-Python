"""for_loop"""

""" A for loop is used for iterating over a sequence (that is either a list, tuple, diictionary, set, or a string)."""

# --------------------------------------------------------------------------------------
"""Python Loops with range()."""
# In Python, a for loop can be used to perform an action a specific number of times in a row.

# The range() function can be used to create a list that can be used to specify the number of iterations
# in a for loop.


"""fibbonacci numbers"""

u = [5, 6]

# for  i(2 to 100)
for i in range(2, 100):  # i = 2 --> 3 --> 4 ...... 99
    # wz calcule with the help of u[i-1] et u[i-2]
    u_i = u[i - 1] + u[i - 2]  # [i-1] = 1 we go to the list ( 1 is 6 in the liste )
    # so we add 5 to 6  = 11

    u.append(u_i)  # use append will add 11 to the list  --> [5,6,11]
print(u)
# after continue the boucle now the list is [5,6,11] so i-1 = 11 and i-2 = 6
# so th new list is [5,6,11,17] etc.

# Print the numbers 0, 1, 2:
for i in range(3):
    print(i)

# Print "WARNING" 3 times:
for i in range(3):
    print("WARNING")


for i in range(10):
    print(f"User number {i + 1}")

# Solution #2
for i in range(1, 11):
    print(f"User number {i}")


# Print the string 12345

n = int(input())

for i in range(n):
    print(i + 1, end="")  # we put i+1 to start from 1 (i+ = 0+1)

# if we did this
n = int(input())

for i in range(n):
    print(i, end="")  # that will print 01234

for i in range(1, 11):
    print(f"i is now {i}")

print("-" * 20)

for j in range(100, 0, -2):
    print(f"i is now {j}")

print("-" * 20)

# to have the nombers from 1 to 10
for x in range(1, 11):
    print(x)


for i in range(5):
    print("python")


# The provided code stub reads and integer,n, from STDIN. For all non-negative integers i<n, print i² .

n = int(input("enter a number"))  # n = 3

for i in range(n):  # --> range (3) = 0,1,2
    print(i * i)  # (i*i) = 0 for 0, 1 for 1 and 4 for 2


n = input("enter your name ")  # string --> ali ( 3 letters)

for i in range(
    len(n)
):  # in this case to have the number of letter we use range(len(n))
    print(i * i)  # (i*i) = 0 for 0, 1 for 1 and 4 for 2

# Else in For Loop
for i in range(3):
    print(i)
else:
    print("finally finished !")
#  0
#  1
#  2
# finally finished !
# -------------------------------------------------------------------------------------
"""For Loop - List"""

bad_marks = [
    0,
    2,
    3,
    3,
    3,
    3,
    4,
    5,
    5,
    5,
    6,
    6,
    6,
    6,
    6,
    7,
    7,
    8,
    8,
    8,
    8,
    8,
    8,
    9,
    10,
    10,
    10,
    11,
    12,
    14,
]

print(len(bad_marks))

total_marks = (
    0  # We give it a value of 0 because we want to use this value in the loop below
)

for i in bad_marks:
    total_marks += i  # it will add all the values ​​of the list to have the result of addition (30)
    print(total_marks)
    moyenne_class = total_marks / 30
print(total_marks)
print(f"la moyenne de la class est {moyenne_class}")

good_marks = []
for n in bad_marks:
    good_marks.append(n + 4)

print(good_marks)


n_total_marks = 0
# Insérez votre code ici
for i in good_marks:
    n_total_marks += i
    moyenne_class = n_total_marks / 30
print(f"la moyenne finale de la class est {moyenne_class}")

# -------------------------------------------------------------------------------------------------------------
values = [61, 20, 45, 63, 96, 71, 6, 8, 72, 22, 97, 7, 46, 11, 15, 74, 81, 69, 70, 26]

# Write your code below
total = 0
for i in values:
    total += i

average = total / len(values)

print(average)
# ----------------------------------------------------------------
# each num in nums will be printed below
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)


# or
# Python3 code to iterate over a list
list = [1, 3, 5, 7, 9]

# getting length of list
length = len(list)


matrix_of_ones = []
for i in range(1):
    matrix_of_ones.append([1, 1, 1])
    for j in range(2):
        matrix_of_ones.append([1, 2, 1])

print(matrix_of_ones)


# Iterating the index
# same as 'for i in range(len(list))'
for i in range(length):
    print(list[i])


RYB_color = ["Red", "Yellow", "Blue"]

for i in RYB_color:
    print(i)
#  Red
#  Yellow
#  Blue


for x in [1, 2, 3, 4]:
    print(x)  # output ( 1,2,3,4 )


a_list = [1, 3, 5]

a_sum = 0  # inside the loop the value increase
for value in a_list:
    a_sum = a_sum + value  # because the new a_sum = old a _sum + value
    print(a_sum)
# output : a_sum = 0 + 1(from list) 1
# a_sum now = 1 + 3(from list) 4
# a_sum now= 4 +5(from list) 9


furniture = ["table", "chair", "rack", "shelf"]

for item in furniture:
    print(item)
# table
# chair
# rack
# shelf

shopping_list = ["milk", "egg", "spam", "pasta"]

for i in shopping_list:
    if i != "spam":
        print("Buy " + i)
else:  # this else is utside the loop
    print("we buy all we want")  # it will print this after the end of the loop

# Output
# Buy milk
# Buy egg
# Buy pasta
# we buy all we want

print("-" * 20)

# or
for i in shopping_list:
    if i == "spam":
        continue
    print(f"Buy {i}")

print("-" * 20)
for i in shopping_list:
    if i == "spam":
        break
    print(f"Buy {i}")


lst = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]

for i in lst:
    for j in i:
        for k in j:
            print(k)


# or
lst = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]

for i in range(0, len(lst)):
    for j in range(0, len(lst[i])):
        for k in lst[i][j]:
            print(k)


print("*" * 20)

lst1 = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]


for i in lst1:
    for j in i:
        print(j)

# ---------------------------------------------------------------------------
""" Getting the index in a loop with enumerate() """
# It is sometimes useful to have access to the index of an element in a sequence. To do this,
#  it is possible to use the enumerate function in the for loop clause:

furniture = ["table", "chair", "rack", "shelf"]

for index, item in enumerate(furniture):
    print(f"index: {index} - item: {item}")
# index: 0 - item: table
# index: 1 - item: chair
# index: 2 - item: rack
# index: 3 - item: shelf


L = [22, 65, 75, 93, 64, 47, 91, 53, 86, 53, 88, 17, 94, 39]

maxi = 0
max_index = 0

# Pour
for index, element in enumerate(L):
    # If the item is bigger than the ones we saw before
    if element > maxi:
        # We replace the maximum by this element
        maxi = element
        max_index = index

print(f"The maximum of the list is at the index {max_index}")

# ------------------------------------------------------------

""" Looping Through Multiple Lists with zip() """
# The zip function allows multiple sequences of the same length to be traversed in parallel in a single for loop.

furniture = ["table", "chair", "rack", "shelf"]
price = [100, 50, 80, 40]

for item, amount in zip(furniture, price):
    print(f"The {item} costs ${amount}")
# The table costs $100
# The chair costs $50
# The rack costs $80
# The shelf costs $40


revenus = [1200, 2000, 1500, 0, 1000, 4500, 1200, 500, 1350, 2200, 1650, 1300, 2300]
depenses = [1000, 1700, 2000, 700, 1200, 3500, 200, 500, 1000, 3500, 1350, 1050, 1850]
economies = []

for revenu, depense in zip(revenus, depenses):
    economie = revenu - depense
    economies.append(economie)

print(economies)
# [200, 300, -500, -700, -200, 1000, 1000, 0, 350, -1300, 300, 250, 450]

#  --------------------------------------------------------------------------
"""For Loop - String"""

for i in "color":
    print(i)
#  c
#  o
#  l
#  o
#  r


names1 = "ali", "hasan"
# the loop takes the first value of (names) and it puts the value in (i) and it prints it
for i in names1:
    # the loop takes the first value of (names) and it puts the value in (i) and it prints it
    print(i)


names2 = "ali", "hasan", "aliiz", "zaid"

for (
    i
) in (
    names2
):  # the loop takes the first value of (names) and it puts the value in (i) and it prints it
    if (
        i == "aliiz"
    ):  # if the value we want to put in (i) = a value in names it makes a validated condition
        break  # it will break that means stop the execution and it will not print this value
    print(i)

for (
    i
) in (
    names2
):  # the loop takes the first value of (names) and it puts the value in (i) and it prints it
    if (
        i == "aliiz"
    ):  # if the value we want to put in (i) = a value in names it makes a validated condition
        continue  # it will do continue which means continue the execution but it ignores this value
    print(i)  # and it does not print it and it continues the execution

# #---------------------------------------------------------------------------------------------------------------------

"""with Dictionaries"""


d = {
    "Race": "Maître du temps",
    "Vaisseau": "TARDIS",
    "nom": "Le Docteur",
    "Origine": "Gallifrey",
}


"""the for loop allows you to browse the keys of the dictionary"""
for x in d:
    print(x)  # result ( Race
    # Vaisseau
    # nom
    # Origine)


"""we could find the values like this"""
for x in d:
    print(d[x])  # resultat (Maître du temps
    # TARDIS
    # Le Docteur
    # Gallifrey)


"""try iterating over the values"""

for x in d.values():
    print(x)
    # resultat (Maître du temps
    # TARDIS
    # Le Docteur
    # Gallifrey)


d1 = {
    "Race": "Maître du temps",
    "Vaisseau": "TARDIS",
    "nom": "Le Docteur",
    "Origine": "Gallifrey",
}


# and key-value pairs?
d1.items()


# Python program to show working of items() method in Dictionary


print("Dictionary items:")

# Printing all the items of the Dictionary
print(d1.items())


# iteration on items
for x, v in d1.items():
    print(x, v)  # Race  Maître du temps
    # Vaisseau  TARDIS
    # nom  Le Docteur
    # Origine  Gallifrey

# with a bit of formatting
for x, v in d1.items():
    print(x, "\t:\t", v)  # Race    :        Maître du temps
    # Vaisseau        :        TARDIS
    # nom     :        Le Docteur
    # Origine         :        Gallifrey


car = {"brand": "ford", "model": "focus", "year": 2013}
for i in car:
    print(i)
# brand
# model
# year

for i in car:
    print(car[i])
# Ford
# Focus
# 2013
# ------------------------------------------------------------------------------------------------------------------
# Write a Python program that sums all values in the matrix stored in variable matrix. Assign the result to a
# variable named total.

matrix = [[0, 9, 5, 4], [8, 2, 3, 0], [1, 5, 3, 2]]

# Write your code below

num_rows = len(matrix)
num_cols = len(matrix[0])

total = 0

for i in range(num_rows):
    for j in range(num_cols):
        total += matrix[i][j]

# -------------------------------------------------------------------------------

row_1 = ["Facebook", 0.0, "USD", 2974676, 3.5]
row_2 = ["Instagram", 0.0, "USD", 2161558, 4.5]
row_3 = ["Clash of Clans", 0.0, "USD", 2130805, 4.5]
row_4 = ["Fruit Ninja Classic", 1.99, "USD", 698516, 4.5]
row_5 = ["Minecraft: Pocket Edition", 6.99, "USD", 522012, 4.5]

app_data_set = [row_1, row_2, row_3, row_4, row_5]
avg_rating = (
    app_data_set[0][-1]
    + app_data_set[1][-1]
    + app_data_set[2][-1]
    + app_data_set[3][-1]
    + app_data_set[4][-1]
) / 5

print(avg_rating)


# if we use For Loop

row_1 = ["Facebook", 0.0, "USD", 2974676, 3.5]
row_2 = ["Instagram", 0.0, "USD", 2161558, 4.5]
row_3 = ["Clash of Clans", 0.0, "USD", 2130805, 4.5]
row_4 = ["Fruit Ninja Classic", 1.99, "USD", 698516, 4.5]
row_5 = ["Minecraft: Pocket Edition", 6.99, "USD", 522012, 6]

app_data_set = [row_1, row_2, row_3, row_4, row_5]

for row in app_data_set:
    rating = row[-1]
    print(rating)


app_data_set = [row_1, row_2, row_3, row_4, row_5]

for row in app_data_set:
    print(row)


# ------------------------------------------------------------------------------
"""searching index with for loop"""

shopping_list = ["milk", "egg", "spam", "pasta"]

item_to_found = "spam"

found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_found:
        found_at = index
        break  # because we found what we search so no need to continue the loop
print(f"item found at the {found_at} position.")

print("-" * 20)
# -----------------------------------------------------------------
# or

shopping_list = ["milk", "egg", "spam", "water"]

item_to_found = "pasta"

found_at = None

if item_to_found in shopping_list:
    found_at = shopping_list.index(item_to_found)
    print(f"item found at the {found_at} position.")

if found_at is not None:
    print(f"item found at position {found_at}")
else:
    print(f"{item_to_found} not found ")

# ----------------------------------------------------------------
"""For Loop - Tuple"""
RYB_color = ("Red", "Yellow", "Blue")
for i in RYB_color:
    print(i)
# >>> Red
# >>> Yellow
# >>> Blue

# ---------------------------------------------------------------------------
"""The break Statement"""

"""In a loop, the break keyword escapes the loop, regardless of the iteration number. Once break executes, 
the program will continue to execute after the loop.

# # In this example, the output would be:"""


numbers = [0, 254, 2, -1, 3]

for num in numbers:
    if num < 0:
        print("Negative number detected!")
        break
    print(num)

# 0
# 254
# 2
# Negative number detected!

RYB_color = ("Red", "Yellow", "Blue")

""" With the break statement we can stop the loop before it has looped through all the items. 
 In this example the loop stopped when the item is equal to yellow"""

for i in RYB_color:
    if i == "Yellow":
        break
    print(i)
# Red

# -----------------------------------------------------------------------------
""" The continue Statement"""

"""In Python, the continue keyword is used inside a loop to skip the remaining code inside the loop code block
and begin the next loop iteration."""

big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

# Print only positive numbers:
for i in big_number_list:
    if i < 0:
        continue
    print(i)


for i in RYB_color:
    if i == "Yellow":
        continue
    print(i)
# Red
# Blue
# With the continue statement we can stop the current iteration of the loop, and continue with the next.

# -------------------------------------------------------------------------------------
"""Nested Loops"""

"""In Python, loops can be nested inside other loops. Nested loops can be used to access items 
of lists which are inside other lists.
The item selected from the outer loop can be used as the list for the inner loop to iterate over."""


groups = [["Jobs", "Gates"], ["Newton", "Euclid"], ["Einstein", "Feynman"]]

# This outer loop will iterate over each list in the groups list
for group in groups:
    # This inner loop will go through each name in each list
    for name in group:
        print(name)


list_1 = ["Data", "Machine Learning"]
list_2 = ["Scientist", "Engineer"]

for i in list_1:
    for j in list_2:
        print(i, j)
# >>> Data Scientist
# >>> Data Engineer
# >>> Machine Learning Scientist
# >>> Machine Learning Engineer


for i in range(
    5
):  # the loop takes the first value of (range) and it puts the value in (i) and it prints(a)
    print("a")
    for j in range(2):  # afterthat it will executes the second loop
        print("b")

# after it returns to the first loop to take the second value of (range) and it re executes the second loop
# then it does the same until the last value of the first loop


for d in range(1, 6):
    for j in range(1, 5):
        print(f"d is now {d} and j is now {j}")

print("-" * 20)


nums = 1, 2, 3
for i in nums:
    print(i)
    for j in nums:
        print(j)

# ------------------------------------------------------------------------------------
for i in range(1, 13):
    for j in range(1, 5):
        print(f"{i} times {j} is {i*j}")
    print("---------------------")

# output
# 1 times 1 = 1
# 1 times 2 = 2
# 1 times 3 = 3
# 1 times 4 = 4
# -------------------------------------------------------------------
# 2 times 1 = 2
# 2 times 2 = 4
# 2 times 3 = 6
# 2 times 4 = 8
# -------------------------------------------------------------------
# 3 times 1 = 3
# 3 times 2 = 6
# 3 times 3 = 9
# 3 times 4 = 12
# -------------------------------------------------------------------
# 4 times 1 = 4
# 4 times 2 = 8
# 4 times 3 = 12
# 4 times 4 = 16
# -------------------------------------------------------------------
# 5 times 1 = 5
# 5 times 2 = 10
# 5 times 3 = 15
# 5 times 4 = 20
# .
# .
# .
# 18 times 1 = 18
# 18 times 2 = 36
# 18 times 3 = 54
# 18 times 4 = 72
# -------------------------------------------------------------------
# 19 times 1 = 19
# 19 times 2 = 38
# 19 times 3 = 57
# 19 times 4 = 76
# -------------------------------------------------------------------

for i in range(1, 11):
    for j in range(5, 7):
        for k in range(1, 3):
            print(f"{i} and {j} and {k}")

# -------------------------------------------------------------------
"""Found the difference between two texts"""

text1 = 'exposes a problem with free speech and online media. Today, with the expand of "technological sphere", anyone can publish anything and based on the free speech, the regulation seem impossible. This problem has been shown in Donald Trump case against Twitter. In fact, president Trump has been banned from the Twitter\'s platform because he published "fake news" about the presidential election and this fakes news created a mob of this supporter who stormed the Capitol. In order to stop that, Twitter\'s banned Donald Trump for encouragement of violence. This case exposes a normative conflict: free speech against freedom of contract. Indeed, Twitter\'s term and service stat that the platform can delete any profile at any time without a justification or appeal process'
text2 = 'Exposes a problem with free speech and online media. Today, with the expand of "technological sphere", anyone can publish anything and based on the free speech, the regulation seem impossible. This problem has been show in Donald Trump case angainst Twitter. In fact, president Trump has been banned from the Twitter\'s plateform because he published "fake news" about presidential election and this fakes news created a mob of this supporter who stormed the Capitol. \nIn order to stop that, Twitter\'s banned Donald Trump for encouragement of violence. This case expose a normative conflict : free speech against freedom of contrat. Indeed, Twitter\'s term and service stat that the plateform can delete any profil at any time without an justification or appel process'

# text1 = 'exposes a problem with free and online media.'
# text2 = 'Exposes a problem with fre online media'
a = text1.replace("\n", "").split(" ")
b = text2.replace("\n", "").split(" ")
Text1_aa = 0
text2_bb = 0
for i in range(0, len(a)):
    tab = [None, None, None, None]  # text1 = None,None,# text2 = None,None
    if Text1_aa < len(a):
        tab[0] = a[Text1_aa]
        if Text1_aa + 1 < len(a):
            tab[1] = a[Text1_aa + 1]

    if text2_bb < len(b):
        tab[2] = b[text2_bb]
        if text2_bb + 1 < len(b):
            tab[3] = b[text2_bb + 1]

    if tab[0] != tab[2]:
        if tab[0] == tab[3]:
            print(tab[0], "**aaa**", tab[2], tab[3])
            text2_bb = text2_bb + 1
        elif tab[1] == tab[2]:
            print(tab[0], tab[1], "**bbb**", tab[2])
            Text1_aa = Text1_aa + 1
        else:
            print(tab[0], tab[2])

    Text1_aa = Text1_aa + 1
    text2_bb = text2_bb + 1
