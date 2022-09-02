"""Functions"""


def multipl():
    return 10.5 * 4


answer = multipl()
print(answer)
# output : 42.0

# or


def multip():
    result = 10.5 * 4
    return result


print(multip())
# output : 42.0


# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def string_test(s):
    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"] += 1
        elif c.islower():
            d["LOWER_CASE"] += 1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["UPPER_CASE"])
    print("No. of Lower case Characters : ", d["LOWER_CASE"])


string_test("The quick Brown Fox")


def mul(x, y):

    result = x * y
    return result


x = int(input("please enter a number"))
y = 4

print(mul(x, y))


# ----------------------------------------------------------------
# Write a Python function that takes a number as a parameter and check the number is prime or not.
def test_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True


print(test_prime(9))


def mltiply(x, y) -> int:
    total = x * y
    return total


print(mltiply(y=5, x=4))

# or


def multiply(x, y):
    result = x * y
    return result


print(multiply(5, 4))


def add_two_numbers() -> int:
    num_one = 3
    num_two = 6
    total = num_one + num_two
    return total


print(add_two_numbers())  # calling a function


# Print the even numbers from a given list
liste = [4, 5, 6, 7, 8, 9]


def test_num(num):
    even_num = []
    for i in num:
        if i % 2 == 0:
            even_num.append(i)
    return even_num


print(test_num(liste))


def generate_full_name() -> str:
    first_name = "Ali"
    last_name = "Ali"
    space = " "
    full_name = first_name + space + last_name
    return full_name


print(f"your name is {generate_full_name()}")  # calling a function

#  we can use the function where we want for example in a for loop
for i in range(5):
    answer = multiply(2, i)
    print(answer)

for i in range(5):
    answer = multiply(y=2, x=i)
    print(answer)


def max_of_two(x, y):
    if x > y:
        return x
    return y


def max_of_threee(x, y, z):
    return max_of_two(x, max_of_two(y, z))


print(max_of_threee(3, 6, -5))


def func(x, y, z):
    result = x * y + (z)
    return result


z = 3


def fun(x, y, z):
    result = x * y + (z)
    return result


print(fun(5, 4, z))

for i in range(5):
    answer = fun(y=2, x=i, z=i)
    print(answer)


# function reverse a string
def string_reverse(str1):

    rev_str = ""
    index = len(str1)
    while index > 0:
        rev_str += str1[index - 1]
        index = index - 1
    return rev_str


print(string_reverse("1234abcd"))


def greet(name, surname) -> str:
    """
    This function greets to the person passed in as a parameter
    """
    name1 = name
    name2 = surname
    space = " "
    full_name = name1 + space + name2
    return full_name


print("oui", greet("aliii", "aliii"))


# Write a Python function to calculate the factorial of a number (a non-negative integer)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input("Input a number to compute the factiorial : "))
print(factorial(n))


# Write a Python function to check whether a number falls in a given range.
def test_range(n):
    if n in range(3, 9):
        print(f"{n} is in the range")
    else:
        print("The number is outside the given range.")


test_range(5)


liste = [8, 2, 3, 7, -1]


def mult(numbers):
    multi = 1
    for i in numbers:
        multi *= i
    return multi


print(mult(liste))


def add(a):
    """
    add 1 to a
    """
    b = a + 1
    print(a, "if you add one", b)
    return b


add(1)


def sum_of_numbers(n):

    total = 0
    for i in range(n + 1):
        print(i)
        total += i
    return total


print("sum", sum_of_numbers(10))  # 55
# print(sum_of_numbers(100)) # 5050


lst = [2, 3, 46, 63, 72, 83, 90, 19]


def is_even(list1):
    even_num = []
    for n in list1:
        if n % 2 == 0:
            even_num.append(n)
    # return a list
    return even_num


# Pass list to the function
even_num = is_even(lst)
print("Even numbers are:", even_num)
# -------------------------------------------------------


def fu(a_list):
    a_list.append(1)


m = []
fu(m)
print(m)
# outputs:
#  [1] because the append method modifies the object on which it is called.
a_list = [5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14]


def f(a_list):
    a_list = a_list + [1]


m = []
f(m)
print(m)
# outputs
# [], because the statement a_list + [1] reassigns a new list to the variable
# rather than to the location it references.


# Indentation is used to identify code blocks
def testfunction(number):
    print("Inside the testfunction")
    sum = 0
    for x in range(number):
        sum += x
    return sum


print("This is not part of testfunction")
print(testfunction(4))

# number=3
# range (3) --> (0,1,2)
# output = 3
# x = 0  --> sum = 0+ 0
# x = 1 --> sum = 0+ 1
# x = 2 --> sum = 1+ 2 =3

# number=4
# range (3) --> (0,1,2,3)
# output = 6
# x = 0  --> sum = 0+ 0
# x = 1 --> sum = 0+ 1
# x = 2 --> sum = 1+ 2 =3
# x = 3 --> sum = 3+ 3 =6


# Function Parameters
def write_a_book(character, setting, special_skill):
    print(character + " is in " + setting + " practicing her " + special_skill)


# Multiple Parameters
def ready_for_school(backpack, pencil_case):
    if backpack == "full" and pencil_case == "full":
        print("I'm ready for school!")


# Define a function my_function() with parameter x
def my_func(x):
    return x + 1


print(my_func(2))  # Output: 3
print(my_func(8))  # Output: 9


# Function Arguments
def sales(grocery_store, item_on_sale, cost):
    print(grocery_store + " is selling " + item_on_sale + " for " + cost)


sales("The Farmer’s Market", "toothpaste", "$1")


# Function Keyword Arguments
def findvolume(length=1, width=1, depth=1):
    print("Length = " + str(length))
    print("Width = " + str(width))
    print("Depth = " + str(depth))
    return length * width * depth


# findvolume(1, 5, 3)
print(findvolume(1, 5, 3))  # output = 15

# findvolume(length=5, depth=2, width=4)
# findvolume(2, depth=3, width=4)


# Returning Multiple Values
def square_point(x, y, z):
    x_squared = x * x
    y_squared = y * y
    z_squared = z * z
    # Return all three values:
    return x_squared, y_squared, z_squared


# three_squared, four_squared, five_squared = square_point(3, 4, 5)
print(square_point(3, 4, 5))  # output (9, 16, 25)


# ----------------------------------------------------------------
# The Scope of Variables
a = 5


def f1():
    a = 2
    print(a)


print(a)  # Will print 5
f1()  # Will print 2

# ----------------------------------------------------------------


# Returning Value from Function
def check_leap_year(year):
    if year % 4 == 0:
        return str(year) + " is a leap year."
    else:
        return str(year) + " is not a leap year."


year_to_check = 2018
returned_value = check_leap_year(year_to_check)
print(returned_value)  # 2018 is not a leap year.

# ----------------------------------------------------------------
"""
Global Variables

A variable that is defined outside of a function is called a global variable. 
It can be accessed inside the body of a function.
In the example, the variable a is a global variable because it is defined 
outside of the function prints_a. It is therefore accessible to prints_a,
which will print the value of a.
"""
a = "Hello"


def prints_a():
    print(a)


# will print "Hello"
prints_a()


# Parameters as Local Variables
def my_function(value):
    print(value)


# Pass the value 7 into the function
my_function(7)

# Causes an error as `value` no longer exists
# print(value)


#  Defining a function in Python - Recipe
def launchpad_welcome():
    print("hello")
    print(1 + 2)
    print(3 + 4)


# Running our function
launchpad_welcome()
# hello
# 3
# 7


# String formatting
print("Welcome {} {}".format("Elon", "Musk"))
# Welcome Elon Musk


names = ["neil armstrong", "buzz aldrin", "sally ride", "yuri gagarin", "elon musk"]


# Positional Arguments
def custom_welcome(name):
    print("Welcome {}".format(name))


custom_welcome("Nick Renotte")
# Welcome Nick Renotte

for name in names:
    custom_welcome(name)
# Welcome neil armstrong
# Welcome buzz aldrin
# Welcome sally ride
# Welcome yuri gagarin
# Welcome elon musk


# Multiple positional Arguments - POSITION IS IMPORTANT
def custom_welcome_to_ship(name, space_ship):
    print("Welcome {} to the {}".format(name, space_ship))


custom_welcome_to_ship("Nick Renotte", "Galatic 1")
# Welcome Nick Renotte to the Galatic 1

space_ships = [
    "Galactic 1",
    "Galactic 2",
    "USS Voyager",
    "Maximum Amazin Wow Space Ship",
    "Apple iShip",
]
# Used the enumerate function to get the positional index AND the name
for idx, name in enumerate(names):
    ship = space_ships[idx]
    custom_welcome_to_ship(name, ship)
# Welcome neil armstrong to the Galactic 1
# Welcome buzz aldrin to the Galactic 2
# Welcome sally ride to the USS Voyager
# Welcome yuri gagarin to the Maximum Amazin Wow Space Ship
# Welcome elon musk to the Apple iShip


# This is using keyword arguments
def space_suit(color="Blue"):
    print("Your space suit is {}".format(color))


space_suit(color="Red")
# Your space suit is Red


# Multiple keyword arguments
def space_suit_welcome(name, space_ship, color="Blue", allergies="None"):
    print(
        f"Welcome {name} to the {space_ship}, your space suit is {color}, you have {allergies} allergies"
    )


space_suit_welcome("Elon Musk", "Apple iShip", allergies="Peanut", color="Orange")
# Welcome Elon Musk to the Apple iShip, your space suit is Orange, you have Peanut allergies


# Setup a return statement
def space_suit_welcome_with_return(name, space_ship, color="Blue", allergies="None"):
    return "Welcome {} to the {}, your space suit is {}, you have {} allergies".format(
        name, space_ship, color, allergies
    )


# Example of storing the results of the function inside a variable
welcome = space_suit_welcome_with_return("Elon Musk", "Apple iShip")
print(welcome)
# Welcome Elon Musk to the Apple iShip, your space suit is Blue, you have None allergies


# Lambda function - anonymous function
pi = lambda x: x * 3.14
return_value = pi(2)
print(return_value)
# 6.28
# 3.14*2
ages = [5, 12, 17, 18, 24, 32]


def myFunc(x):
    if x < 18:
        return False
    else:
        return True


adults = filter(myFunc, ages)
for x in adults:
    print(x)

# -----------------------------------------------------------------------------------------------*


# function creation
def cree_list(taille):
    list(range(taille))


# function call
cree_list(12)
cree_list(taille=12)
print(cree_list(12))


def cree_listee(taille):
    return list(range(taille))


# now it returns
cree_listee(12)
cree_listee(taille=12)


# the function can be called anywhere i can use the resulting data type
for x in cree_listee(12):
    print(x)

# # parameters are required
# cree_listee()


# Let's create an optional parameter with a default value
def cree_liste(taille):
    return list(range(taille))


# ----------------------------------------------------------------
"""*args and *kwargs* are ( the * mean one value (tuple) and the ** mean key value (dict) )"""


def fun1(p1, p2, *args, k, **kwargs):
    print(f"the first value p1 = {p1}")
    print(f"the second value p2 = {p2}")
    print(f"the third value *args = {args}")  # it's like a tuple
    print(f"the fourth value k = {k}")
    print(f"the fifth value **kwargs = {kwargs}")  # it's like a dictionary


fun1(1, 2, 3, 4, 5, 6, k=10, key1="name", key2="ali")
# the first value p1 = 1
# the second value p2 = 2
# the third value *args = (3, 4, 5, 6)
# the fourth value k = 10
# the fifth value **kwargs = {'key1': 'name', 'key2': 'ali'}


def fun2(p1, p2, *integer, k, **dic):
    print(f"the first value p1 = {p1}")
    print(f"the second value p2 = {p2}")
    print(f"the third value *args = {integer}")  # it's like a tuple
    print(f"the fourth value k = {k}")
    print(f"the fifth value **kwargs = {dic}")  # it's like a dictionary


fun2(1, 2, 3, 4, 6, k=10, key1="name", key2="ali")
# the first value p1 = 1
# the second value p2 = 2
# the third value *args = (3, 4, 6)
# the fourth value k = 10
# the fifth value **kwargs = {'key1': 'name', 'key2': 'ali'}


def my_sum(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result


list_of_integers = [1, 2, 3]
print(my_sum(list_of_integers))


def my_sum1(*integers):
    result = 0
    # Iterating over the Python args tuple
    for x in integers:
        result += x
    return result


print(my_sum1(1, 2, 3))


def my_sum2(*args):
    result = 0
    for x in args:
        result += x
    return result


list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]

print(my_sum2(*list1, *list2, *list3))


# let's create a "free" dictionary parameter
""" **d it's like **kwargs that's mean tow arguments (key, value) to create a dictionary"""


def cree_lst(taille=10, **d):
    return d


cree_lst(taille=3)
cree_lst(taille=10, nom="Les Docteur", Vaisseau="TARDIS")

# ----------------------------------------------------------------
"""
Define a function max() that takes two numbers as arguments and returns the largest of them.
Use the if-then-else construct available in Python.
(It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)
"""


def max(a, b):

    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "bonne chance"


if __name__ == "__main__":
    print(max(6, 5))
    print(max(2, 5))
    print(max(5, 2))
    print(max(5, 5))


"""
Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
"""


# from ex1 import max
def max_of_three(a, b, c):
    max_temp = max(a, b)
    return max(max_temp, c)


if __name__ == "__main__":
    print(max_of_three(1, 2, 3))


"""
Define a function that computes the length of a given list or string.
(It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)
"""


def lenghth(string):
    count = 0
    for i in string:
        count += 1
    return count


if __name__ == "__main__":
    print(lenghth("good days will come! :)"))

# ------------------------------------------------------------------------------------------------
# (a) Implement a function named double which takes a number as argument and returns its double.
# (b) Use this function to calculate the double of 4.


def double(nombre):
    double = nombre * 2
    return double


double(nombre=4)
# --------------------------------------------------------------------------------
# (c) Write a function named list_product that takes a list of numbers as an argument and loops through the product of all the numbers in the list.
# (d) Evaluate this function on the list [1, 0.12, -54, 12, 0.33, 12]. Its result should be -307.9296.


test_list = [1, 0.12, -54, 12, 0.33, 12]


# Insérez votre code ici
def liste_product(liste_de_nombres):

    nombre_list = 1
    for i in liste_de_nombres:
        nombre_list *= i
    return nombre_list


print(liste_product(test_list))
# ----------------------------------------------
# Write a function named unique that takes a list as an argument and returns a new list containing the unique values ​​of that list.
# Single value does not mean values ​​that appear only once in the list but rather distinct values.

# So unique([1, 1, 2, 2, 2, 3, 3, "Hello"]) should return [1, 2, 3, "Hello"].

# This terminology is very often used even if it does not have the same meaning as in everyday life.

# You can check if an item is part of a list using the in membership operator:
# 3 in [3, 1, 2]
# # >>> True

# -1 in [3, 1, 2]
# # >>> False


def uniques(liste):

    unique = []
    for element in liste:

        if element not in unique:

            unique.append(element)

    return unique


print(uniques([1, 1, 2, 2, 2, 3, 3, "Bonjour"]))

# -----------------------------------------------------------
# A function can have multiple parameters and multiple outputs.
# The general syntax of a function is therefore as follows:
"""def ma_fonction(paramètre1, paramètre2, paramètre3 ...):"""
# Bloc d'instructions
# ...
# ...
# ...
# return sortie1, sortie2, sortie3...


# When a function returns multiple outputs, the result of the function is actually a tuple. We can use the assignment tuple to store the outputs in different variables:

# Defining a function that returns the first and last element of a list
def first_and_last(a_list):
    return a_list[0], a_list[-1]


# Using the assignment tuple to retrieve the outputs of the function
first, last = first_and_last([-2, 32, 31, 231, 4])

print(first)
# >>> -2

# print(last)
# >>> 4

# ----------------------------------------------------------------

# Create a power4 function, which takes a number x as argument and returns the first 4 powers of this number ( x1,x2,x3,x4x1,x2,x3,x4 ).
# (g) Test this function on x = 8 and store the results in x_1, x_2, x_3 and x_4.
# (h) Create a function power_diff taking as argument 4 numbers x_1, x_2, x_3 and x_4 and which returns the difference between x_2 and x_1, the difference between x_3 and x_2 and the difference between x_4 and x_3.
# (i) Test this function on the values ​​x_1, x_2, x_3 and x_4 obtained previously.


def power4(x):
    return x ** 1, x ** 2, x ** 3, x ** 4


# print(power4(2))
# # (2, 4, 8, 16)

x_1, x_2, x_3, x_4 = power4(x=8)


def power_diff(x_1, x_2, x_3, x_4):
    dif1 = x_2 - x_1
    dif2 = x_3 - x_2
    dif3 = x_4 - x_3

    return dif1, dif2, dif3


dif1, dif2, dif3 = power_diff(x_1, x_2, x_3, x_4)

print(f"dif1 est {dif1}, dif2 est {dif2}, dif3 est {dif3}")

# ----------------------------------------------------------

# When calling a function, it is possible not to specify the value of a parameter if it has a default value.

# To give a parameter a default value, simply assign it a value in the function definition:

# Définition d'une fonction qui calcule le produit entre deux nombres
def produit(a=0, b=1):
    return a * b


# produit(a=4) # Par défaut, b prend la valeur 1
# >>> 4

# produit(b=3) # Par défaut, a prend la valeur 0
# >>> 0

# produit(a=4, b=3)
# >>> 12

# It is not necessary to write the name of the parameters when calling a function (e.g. product(3, 4) returns 12), but in this case the parameters must follow the same order as in the definition of the function


# ---------------------------------------------------------------------------

"""Documentation of a function
In order to share a function with other users, it is common to write a short description that explains how the function should be used.

This description is called the documentation of a function.

Documentation is written at the beginning of a function definition:"""
# def sort_list(a_list, order = "ascending"):
#     """
#     Cette fonction trie une liste dans l'ordre spécifié par l'argument 'order'.

#     Paramètres:
#         a_list : la liste à trier.

#         order : Doit prendre la valeur "ascending" si on veut trier la liste dans l'ordre croissant.
#                 Doit prendre la valeur "descending" sinon.

#     Renvoie :
#         La même liste mais triée.
#     """
#     # instructions
#     ...
#     ...
#     ...
#     return sorted_list

# The triple quotes """ define the beginning and end of the documentation.

# You can view a function's documentation using Python's help function.

# (a) View documentation for Python's len function. A "container" designates any object on which one can iterate such as a list, a tuple, a character string, etc...
# (b) Write a function total_len which takes a list of lists as argument and determines the total number of elements in this list. Write a small documentation that describes its use.
# -------------------------------------------------------------------

"""Test this function on the list:"""
# test_list = [[1, 23, 1201, 21, 213 ,2],
#                [2311, 12, 3, 4],
#                [11 , 32, 1, 1, 2, 3, 3],
#                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
# La fonction total_len devrait renvoyer 31.
# Afficher la documentation de la fonction len de Python.
help(len)


def total_len(liste_de_listes):
    """
    Cette fonction détermine le nombre total d'éléments dans une liste de listes
    """
    n_elements = 0

    for liste in liste_de_listes:

        n_elements += len(liste)

    return n_elements


test_list = [
    [1, 23, 1201, 21, 213, 2],
    [2311, 12, 3, 4],
    [11, 32, 1, 1, 2, 3, 3],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

total = total_len(test_list)

print(f"La liste test_list contient{total} éléments.")

# ----------------------------------------------------------------

"""Recursive functions"""
# Recursion is the property for a function to evaluate itself within its own definition.

# This kind of syntax is able to solve some problems very simply, but is no longer widely used in Python.

# The idea of ​​recursive functions is to simplify a problem until the solution is trivial.

# For example, if N people must shake hands to greet each other, how many handshakes took place?

# Suppose one person among the N shook hands with the other N-1 people. We already count N-1 handshakes and it is now enough to count the handshakes for the remaining N-1 people.

# Count this way until there are only 2 people left. In this case there is only one possible handshake left.

# In Python, to count the number of handshakes between N people, we can define a recursive function:
def combien_de_poignees(N):
    # Si il n'y a que 2 personnes
    if N == 2:
        # Il ne peut y avoir qu'une seule poignée de main
        return 1
    # Sinon
    else:
        # On compte N-1 poignées de main + le nombre de poignées de main
        # entre les N-1 personnes restantes
        return N - 1 + combien_de_poignees(N - 1)


# This function gives us an easy solution to this problem.
# ----------------------------------------------------------------

# Define a factorial recursive function which at a number nn calculates its factorial n!=1×2×...×nn!=1×2×...×n:
# You will notice the recurrence n!=n×(n−1)!n!=n×(n−1)! .
# We assume that 0!=10!=1 .
# (b) Calculate 5! (5!=120)


def factoriellee(n):
    if n < 0:
        return "Nombre négatif ou nul"  # arrête la fonction si l'input est négatif

    if n == 0:
        return 1
    else:
        return n * factorielle(n - 1)


print(factoriellee(n=5))

# or


def factorielle(n):

    if n == 0:
        return 1
    elif n < 0:
        return "Nombre négatif ou nul"

    else:
        return n * factorielle(n - 1)


print(factorielle(n=5))

# ----------------------------------------------------------------
"""function calling function"""


def funn(txt):
    string = ""
    for i in txt:
        if i.isalnum():  # that's mean char with no spaces and no ( , - . ...)
            string += i
            print(string)
        else:
            print(i)
    return (
        string[::-1].casefold() == string.casefold()
    )  # that's means True (if we reverse the string == the string)


word = "was it a car, or a cat, i saw"
if funn(word):  # if true
    print("true")
else:
    print("false")
# w
# wa
# was

# wasi
# wasit

# wasita

# wasitac
# wasitaca
# wasitacar
# ,

# wasitacaro
# wasitacaror

# wasitacarora

# wasitacarorac
# wasitacaroraca
# wasitacaroracat
# ,

# wasitacaroracati

# wasitacaroracatis
# wasitacaroracatisa
# wasitacaroracatisaw
# true


# now to use the function call function
def rev(string):
    return string[::-1].casefold() == string.casefold()


def g(txt):
    string = ""
    for i in txt:
        if i.isalnum():  # that's mean char with no spaces and no ( , - . ...)
            string += i
            print(string)
        else:
            print(i)
    return rev(string)


word = "was it a car, or a cat, i saw"
if g(word):  # if true
    print("true")
else:
    print("false")


# -------------------------------------------------------
# Write a Python program that invoke a given function after specific milliseconds.


import math
from time import sleep


def delay(fn, ms, *args):
    sleep(ms / 1000)
    return fn(*args)


print("Square root after specific miliseconds:")
print(delay(lambda x: math.sqrt(x), 100, 16))
print(delay(lambda x: math.sqrt(x), 1000, 100))
print(delay(lambda x: math.sqrt(x), 2000, 25100))
