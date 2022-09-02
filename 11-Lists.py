"""Lists"""
# --------------------------------------------------------------------------
"""merging_lists"""
my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
my_merged_list = [*my_first_list, *my_second_list]

print(my_merged_list)


# extract_list_body.py
my_list = [1, 2, 3, 4, 5, 6]

a, *b, c = my_list

print(a)
print(b)
print(c)

# 1
# [2, 3, 4, 5]
# 6
# -----------------------------------------------------------------------
"""methods"""
employes = ["Carlos", "Max", "Martine", "Patrick", "Alex", "Max"]
employes.index("Alex")  # 4
employes.count("Max")  # 2
employes.sort()  # Sort the list by modifying it directly : ["Alex", "Carlos", "Martine", "Max", "Max", "Patrick"]
sorted(employes)  # Sorts the list but does not modify the original list!
liste_trie = sorted(employes)  # We return the sorted list in a new list.

employes.pop(3)
employes.insert(1, "Hello")

nombres = [10, 1, 5, 15]
nombres.reverse()  # Reverse the order of the list : [15, 5, 1, 10]
print(nombres)

liste = [5]
liste.append(3)  # [5, 3]
liste.extend([20, "Python"])  # [5, 3, 20, "Python"]
liste.remove("Python")  # [5, 3, 20]

liste = [5, 3, 20]
liste.sort(reverse=True)
print(liste)
# [20, 5, 3]

# ----------------------------------------------------------------
utilisateurs = ["Richard", "Paul", "marie"]
utilisateurs.sort()
print(utilisateurs)
# output ['Paul', 'Richard', 'marie']
# -------------------------------------
# if we use casefold
utilisateurs = ["Paul", "Richard", "marie"]
utilisateurs.sort(key=str.casefold)
print(utilisateurs)
# output ['marie', 'Paul', 'Richard']
# ------------------------------------------------------------------------------------------------
liste = ["Python", "est", "un", "langage", "incroyable"]

" ".join(liste)  # 'Python est un langage incroyable'
" - ".join(liste)  # Python - est - un - langage - incroyable
"".join(liste)  # Pythonestunlangageincroyable

resultat = "\n".join(liste)
print(resultat)
# Python
# est
# un
# langage
# incroyable
# ----------------------------------------------------
liste = ["Python", ["Java", "C++", ["C"]], ["Ruby"]]

liste[0]  # 'Python'
liste[-1][0]  # 'Ruby'
liste[0][0:2]  # 'Py'
liste[1][1]  # 'C++'
liste[1][:2]  # ['Java', 'C++']
# ----------------------------------------------------------------
""""slices"""
liste = [
    "Utilisateur_01",
    "Utilisateur_02",
    "Utilisateur_03",
    "Utilisateur_04",
    "Utilisateur_05",
    "Utilisateur_06",
]

liste[
    :
]  # ['Utilisateur_01', 'Utilisateur_02', 'Utilisateur_03', 'Utilisateur_04', 'Utilisateur_05', 'Utilisateur_06']
liste[
    1:
]  # ['Utilisateur_02', 'Utilisateur_03', 'Utilisateur_04', 'Utilisateur_05', 'Utilisateur_06']
liste[:1]  # ['Utilisateur_01']
liste[1:3]  # ['Utilisateur_02', 'Utilisateur_03']
liste[1:-1]  # ['Utilisateur_02', 'Utilisateur_03', 'Utilisateur_04', 'Utilisateur_05']


list_1 = [
    [
        "Utilisateur_01",
        "Utilisateur_02",
        "Utilisateur_03",
        "Utilisateur_04",
        "Utilisateur_05",
        "Utilisateur_06",
    ],
    [1, 2, 3, 4, 5, 6],
    ["Carlos", "Max", "Martine", "Ali", "Patrick", "Max"],
]

result1 = list_1[0][2]
result2 = list_1[1][2]
result3 = list_1[2][3]

print(result1)  # Utilisateur_03
print(result2)  # 3
print(result3)  # Ali
# ------------------------------------------------------------------------------------------------
"""operators with lists"""

utilisateurs = ["Paul", "Pierre", "Marie"]
"Paul" in utilisateurs  # returns the Boolean True

if "Paul" in utilisateurs:
    print("Bonjour Paul, bon retour parmi nous!")

if "Paul" in utilisateurs:
    utilisateurs.remove("Paul")

# Also works with strings
"Java" in "Javascript"  # returns the Boolean True
# ----------------------------------------------------------------
"""sorted list"""
sentence = "The quick brown fox jumps over the lazy dog"

letters = sorted(sentence)
print(letters)


numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]

sorted_numbers = sorted(numbers)
print(sorted_numbers)  # here will print the list sorted

print(numbers)

numbers.sort()  # here will print the list sorted with change the original list
print(numbers)

missing_letter = sorted("The quick brown fox jumps over the lazy dog", key=str.casefold)
print(missing_letter)
# ------------------------------------------------------------
"""add and remove to list"""
liste = [5]
liste.append(3)  # [5, 3]
liste.extend([20, "Python"])  # [5, 3, 20, "Python"]
liste.remove("Python")  # [5, 3, 20]
# ----------------------------------------------------------------
"""delete item list """
data = [4, 5, 8, 9, 55, 66, 98, 77, 22, 33, 12, 54, 478, 986]

del data[0:5]
print(data)

min_valid = 1

max_valid = 100

data_new = []
for i in data:
    if i > min_valid and i < max_valid:
        data_new.append(i)

print(data_new)

# print("-"*50)
# ----------------------------------------------------------------
# or

data1 = [455, 102, 98, 77, 192, 330, 120, 54, 478, 986]

min_valid_1 = 100
max_valid_1 = 200

for index in range(len(data1) - 1, -1, -1):  # (-1 to begain from the last item of list)
    # the second -1 to finish in the first item of the list
    # the third -1 it's the step
    # print(index)
    if data1[index] < min_valid_1 or data1[index] > max_valid_1:
        print(index, data1)
        del data1[index]

print(data1)

print("-" * 50)
# ----------------------------------------------------------------
# or
data2 = [455, 126, 77, 114, 155, 192, 330, 120, 54, 478, 986]

min_valid_2 = 100
max_valid_2 = 200


top_index = len(data2) - 1
for index, value in enumerate(reversed(data2)):
    if value < min_valid_2 or value > max_valid_2:
        print(top_index - index, value)
        del data2[top_index - index]

print(data2)

# -------------------------------------------------------------
employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"]
element = employes.pop(
    -1
)  # removes the last element of the list (here, "Alex") and returns it in the variable 'element'
print(element)  # show the name 'Alex'
print(employes)  # ["Carlos", "Max", "Martine", "Patrick"]
employes.clear()  # remove all items from the list


ma_liste = [1, 5, "Bonjour", -1.4, "ça", 103, "va"]

# Insérez votre code ici
ma_liste.pop(2)
ma_liste.pop(3)
ma_liste.pop(4)  # or  ma_liste.pop(-1)

print(ma_liste)


ma_liste = [1, 5, "Bonjour", -1.4, "comment", "ça", 103, "va"]


ma_liste.pop(0)

ma_liste.pop(0)

ma_liste.pop(1)

ma_liste.pop(3)

# ma_liste = ["Bonjour", "comment", "ça", "va"]

ma_liste.insert(1, "Hello")
# ma_liste = ["Bonjour","Hello", "comment", "ça", "va"]


ma_liste.insert(3, "how")
# ma_liste = ["Bonjour","Hello", "comment","how", "ça", "va"]

ma_liste.insert(5, "are")
# ma_liste = ["Bonjour","Hello", "comment","how", "ça","are", "va"]

ma_liste.insert(7, "you")
# ma_liste = ["Bonjour","Hello", "comment","how", "ça","are", "va","you"]
# Affichage de la liste

print(ma_liste)

# ----------------------------------------------------------------------------------------------------------------

# It is possible to add an item directly to (the end of a list) using the append method.
x = 0
une_liste = [x]

x = x + 1
une_liste.append(x)
print(une_liste)  # output [0] after second execution [0,1] , third exex [0,1,2]

# ----------------------------------------------------------------------------------------------------------------
# To merge two lists, we can use the extend method. The argument of the extend method is a list of items that we want to add to the end of the list calling the method.

### Fusion de 2 listes avec la méthode extend

liste_1 = ["Bonjour", "comment", "ça", "va", "?"]
liste_2 = ["Bien", "et", "toi", "?"]

liste_1.extend(liste_2)

print(liste_1)

# or (not recommended)
liste_1 = ["Bonjour", "comment", "ça", "va", "?"]
liste_2 = ["Bien", "et", "toi", "?"]

liste_1 = liste_1 + liste_2
print(liste_1)
# ----------------------------------------------------
computer_parts = ["computer", "monitor", "keyboard", "mouse"]

for part in computer_parts:
    print(part)

print()  # to have a space
print(computer_parts[2])

parts_1 = parts_2 = computer_parts

parts_2.append("sound")

print(parts_1)

print(parts_2)

# ----------------------------------------------------------------
shopping_list = ["bread", "milk", "pasta", "rice"]

another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))
# -------------------------------------------------------
"""replacing-slice"""
computer_parts = ["computer", "monitor", "keyboard", "mouse"]

print(computer_parts)

print(computer_parts[2])
computer_parts[2] = "case"

print(computer_parts)

computer_parts[2:] = "keyboard"
print(computer_parts)

computer_parts[2:] = ["keyboard"]
print(computer_parts)


# ---------------------------------------------------
"""number list"""
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# print(min(even))
# print(max(even))
# print(min(odd))
# print(max(odd))
#
# print()
#
# print(len(even))
# print(len(odd))
#
# print("missisippi".count("s"))

even.extend(odd)
print(even)

even.sort()
print(even)

even.sort(reverse=True)
print(even)

# ---------------------------------------------------------------
"""append lists"""
available_parts = ["computer", "monitor", "mouse", "keyboard"]
current_choice = "-"
computer_parts = []

while current_choice != "0":

    if current_choice in "12345":
        print(f"adding {current_choice}")
        if current_choice == "1":
            computer_parts.append("computer")
        elif current_choice == "2":
            computer_parts.append("monitor")
        elif current_choice == "3":
            computer_parts.append("mouse")
        elif current_choice == "4":
            computer_parts.append("keyboard")

    else:
        print("please add option from the list below:")
        print("1\tcomputer")
        print("2\tmonitor")
        print("3\tmouse")
        print("4\tkeyboard")
    current_choice = input()
    print(computer_parts)

# print("-"*50)
# --------------------------------------------------------
# or
available_parts = ["computer", "monitor", "mouse", "keyboard"]
current_choice = "-"
computer_parts = []

while current_choice != "0":

    if current_choice in "12345":
        print(f"adding {current_choice}")
        if current_choice == "1":
            computer_parts.append("computer")
        elif current_choice == "2":
            computer_parts.append("monitor")
        elif current_choice == "3":
            computer_parts.append("mouse")
        elif current_choice == "4":
            computer_parts.append("keyboard")

    else:
        print("please add option from the list below:")
        for part in available_parts:
            print(
                f"{available_parts.index(part)+1} {part}"
            )  # We put+1 because index start from 0,but need start from 1

    current_choice = input()
    print(computer_parts)
# --------------------------------------------------------
# or
available_parts = ["computer", "monitor", "mouse", "keyboard"]
current_choice = "-"
computer_parts = []

while current_choice != "0":

    if current_choice in "12345":
        print(f"adding {current_choice}")
        if current_choice == "1":
            computer_parts.append("computer")
        elif current_choice == "2":
            computer_parts.append("monitor")
        elif current_choice == "3":
            computer_parts.append("mouse")
        elif current_choice == "4":
            computer_parts.append("keyboard")

    else:
        print("please add option from the list below:")
        for number, part in enumerate(available_parts):
            print(
                f"{number+1} {part}"
            )  # We put+1 because index start from 0,but need start from 1

    current_choice = input()
    print(computer_parts)

print("-" * 50)

# --------------------------------------------------------------------------
# or use list comprehension

available_parts = ["computer", "monitor", "mouse", "keyboard"]

valid_choice = [str(i) for i in range(1, len(available_parts) + 1)]
print(valid_choice)
current_choice = "-"
computer_parts = []

while current_choice != "0":
    if current_choice in valid_choice:
        # print(f"adding {current_choice}")
        index = (
            int(current_choice) - 1
        )  # -1 because we put a +1 in valid choice to start the index from 1 not from 0
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

