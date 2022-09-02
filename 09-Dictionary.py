# Dictionary
# Dictionary example
# Car = {
#       "­bra­nd": "­For­d",
#       "­mod­el": "­Foc­us",
#       "­yea­r": 2013
# }
# print(Car)
# >>>­{'b­rand': 'Ford', 'model': 'Focus', 'year': 2013}
# The dict() Constr­uctor
# thisdict = dict(b­ran­d="F­ord­", model=­"­Foc­us", year=2013)
# Accessing Items
# Example 1
# x = Car["mo­del­"]
# Example 2
# x = Car.ge­t("m­ode­l")
# Change Values
# Car["ye­ar"] = 2019
# Check if Key Exists
# Check if "­yea­r" is present in the dictio­nary:
# if "­yea­r" in Car:
#  ­ ­ ­ ­pri­nt(­"Yes, 'year' is one of the keys in the Car dictio­nar­y")
# Dictionary Length
# print(­len­(Car))
# >>> 3
# Adding Items
# Car["Co­mbined MPG"] = 32

# Removing Items
# Car.po­p("y­ear­")
# The pop() method removes the item with the specified key name
# Car.po­pitem()
# The popitem() method removes the last inserted item
# del Car["ye­ar"]
# The del keyword removes the item with the specified key name
# Delete a Dictionary
# del Car
# print(­Cars) #this will cause an error because "­Car­s" no longer exists.
# Return an Empty Dictionary
# Car.cl­ear()
# Copy a Dictionary
# Example 1
# CarCopy = Car.copy()
# Example 2
# CarCopy = dict(Car)

# Nested Dictio­naries
# Cars = {
#    ­ ­  "­Car­1":{
#  ­ ­ ­ ­  "brand":"Ford",
#  ­ ­ ­ ­  "­mod­el":­"­Foc­us"
#  ­ ­ ­   },
#    ­ ­  "­Car­2":{
#  ­ ­ ­ ­  "brand":"Fiat",
#  ­ ­ ­ ­  "­mod­el":­"­Pun­to"
#  ­ ­ ­   }
#  ­ }
# Create a nested dictionary from two existing dictio­nai­ries.
# Car1 = {
#       "­bra­nd": "­For­d",
#       "­mod­el": "­Foc­us"
# }
# Car2 = {
#       "­bra­nd": "­Fia­t",
#       "­mod­el": "­Pun­to"
# }
# Cars = {
#       "­Car­1": Car1,
#       "­Car­2": Car2
# }


# un_dict = {"age" : 25, "taille" : 183, "sexe" : "F", "prenom" : "Vanessa"}

# # Affichage des éléments
# print(un_dict["age"])
# print(un_dict["prenom"])


# carte_id = {"prenom":"paul", "nom":"lefebvre", "emission":1978}
# print(carte_id)

# carte_id["prenom"] = "guillaume"
# print(carte_id)

carte_id = {"prenom": "paul", "nom": "lefebvre", "emission": 1978}
carte_id["expiration"] = 1993
print(carte_id)

validité = carte_id["expiration"] - carte_id["emission"]
print(f"la duree de validité est {validité } ans")


# ----------------------------------------------------------------
# let's create a "free" dictionary parameter
""" **d it's like **kwargs that's mean tow arguments (key, value) to create a dictionary"""


def cree_lst(taille=10, **d):
    return d


cree_lst(taille=3)
cree_lst(taille=10, nom="Les Docteur", Vaisseau="TARDIS")
# ----------------------------------------------------------------

"""merging_dicts"""

my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}
my_merged_dict = {**my_first_dict, **my_second_dict}

print(my_merged_dict)
