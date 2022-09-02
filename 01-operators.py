"""Operators"""


# Distance en km entre Paris et Marseille
distance = 750

# Vitesse moyenne d'un marcheur en km/h
vitesse = 4.8

# Temps en heures qu'il faudrait pour aller de Paris à Marseille sans s'arrêter
temps = distance / vitesse

# Nombre de jours de marche
jours = temps // 24

# Nombre d'heures restantes
heures_restantes = temps % 24

# or

# jour = temps / 24
# jours = temps // 24


# heures_restantes= (jour - jours)* 24
# print(f"Il faudrait au marcheur {jour} jours et {heures_restantes} heures.")


print("Il faudrait au marcheur", jours, "jours et", heures_restantes, "heures.")


num1 = 10  # int

num2 = 3.5  # float

name = "ali"  # str

a = input("enter something ")  # give an str value to the input
print(a)
print(type(a))  # Str


a = int(input("enter a number "))  # give an int  value to the input
print(a)
print(type(a))  # int


n = 5
x = 3 ** (2 * n + 1) + 2 ** (4 * n + 2)
print(x % 7 == 0)  # output = True


nombres_premiers = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
x = nombres_premiers[0]

# Insérez votre code ici
x **= 2  # output = (x = x**2)

x += 17
print(x)  # output = 42

x %= 12

print(x)  #  output = 6 ----> 42 % 12 -> output =(12*4 =48) --> modulo = 6


a, b = 12, 5  # -->  the same a=12 and b=5

print(a + b)
print(a - b)
print(a * b)
print(a / b)  # the result is float
print(a // b)  # the result is integer
print(a % b)  # modulo (--> 5*2 = 10 and the rest for 12 is 2)

for i in range(1, 4):
    print(i)


# for i in range(1,a/b): #this will gave us an error because we use integer with float
#     print(i)

for i in range(1, a // b):
    print(i)


# The provided code stub reads two integers,  and , from STDIN.
# Add logic to print two lines. The first line should contain the result of integer division,  // .
# The second line should contain the result of float division,  / .
# No rounding or formatting is necessary.

a = int(input("enter the first number "))
b = int(input("enter the second number "))

c = a // b

print(c)

d = a / b

# Exponentiation  ( ** )

num7 = 2
num8 = 5

# same as 2*2*2*2*2

num9 = 5
num10 = 2

print(num9 ** num10)  # same as 5*5 (result = 25)


une_liste = [1, 3, 102, 32, 11, -12, 33]
x = 14

# Est-ce que la valeur de x fait partie des valeurs de une_liste ?
print(x in une_liste)
# False

# Est-ce que la valeur de x ne fait PAS partie des valeurs de une_liste ?
print(x not in une_liste)
# True

# -------------------------------------------------------------------------------------------
""" Python -- Priorities"""

# python will compare the operations from left to right and it will compare the two operations
# ( / is stronger than * and * is stronger than +)


num1 = 10 + 5 * 3  # ( * is stronger than +)
# then we start the operation by multiplying 5 * 3 then we do the addition with 10

print(num1)  # (result = 25)


num2 = (
    10 + 5 * 5 / 2
)  # ( * is stronger than +) we start the operation by multiplying 5 * 5
# after (the result / 2) and finally we do the addition with 10

print(num2)  # (result = 22.5)


num3 = (
    10 / 5 * 3
)  # ( * is stronger than +) we start the operation by dividing 10 / 5 and then ( the result * 3 )
# the answer is float because we used division by (a single slash / )

print(num3)  # (result = 6.0)


num4 = 10 // 5 * 3
# we start the operation by dividing 10 // 5 and then (the result * 3)
# the answer is integer because we used division by ( double slash // --> floor division)

print(num4)  # (result = 6)


num5 = 10 / 5 - 1  # ( / is stronger than -)
# then we start the operation by dividing 10 / 5 then we do the Subtraction with 1

print(num5)  # (result = 1.0)


num6 = 16 - 2 * 5 // 3 + 1
# the expression is evaluated as (2*5) first, then (10 // 3), then (16-3), and then (13+1).

# print(num6) #(result = 14)
# ---------------------------------------------------------------------------------------------------
"""Logical Operators"""
# Insérez votre code ici

# personne1 ( Bernadette )
anciennete = 12
salaire = 2400

critère1 = anciennete < 5 and salaire <= 1500


critère2 = 5 <= anciennete <= 10 and 1500 < salaire < 2300

critère3 = 10 < anciennete and 1500 > salaire or salaire > 2300

print(
    f"Est ce que Bernadette a le droit d'un prime dans ces cas: critère1:{critère1} or critère2:{critère2} or critère3:{critère3}?"
)


# personne2 ( Marc )

anciennete = 6
salaire = 1490

critère1 = 5 > anciennete and salaire < 1500

critère2 = 5 <= anciennete <= 10 and 1500 <= salaire <= 2300

critère3 = anciennete > 10 and 1500 > salaire or salaire > 2300

print(
    f"Est ce que Marc a le droit d'un prime dans ces cas: critère1:{critère1} or critère2:{critère2} or critère3:{critère3}?"
)

# -----------------------------------------------------------------------------------------------------
"""Control Structures"""
eligible = False
solde = 0

# Est-ce que le fonctionnaire est éligible à la prime ?
if eligible == True:
    solde += 300
    # Si oui, on augmente son solde de 300 euros
# Suite à de nombreuses plaintes, le gouvernement va quand même offrir une prime de 50€ aux personnes qui ne sont pas éligibles à la prime de 300€. Afin de créditer le compte de ces gens-là, nous allons ajouter une clause else à notre programme, dont les instructions associées s'exécuteront si eligible vaut False :

# Est-ce que le fonctionnaire est éligible à la prime ?
if eligible == True:
    solde += 300
    # Si oui, on augmente son solde de 300 euros
else:
    solde += 50
    print(solde)
    # Sinon, on n'augmente son solde que de 50 euros

note = 4

if note < 5:
    print("Travail très insuffisant.")
elif note < 10:
    print("Peut mieux faire.")
elif note < 15:
    print("Du bon travail. Je vous encourage à continuer ainsi.")
else:
    print("Excellent travail. Toutes mes félicitations.")
