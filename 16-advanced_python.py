"""Annotations"""

"""Type in programming"""

# ------------------------------------------------------------------------------------------------
"""type int"""

a = 2
type_of_a = type(a)

# The type of the argument is displayed using the print function as:
# <class 'int'>

"""type str"""

b = "bonjour"
print(type(b))

# The type of the argument is displayed using the print function as:
# <class 'str'>

# ------------------------------------------------------------------------------------------------
"""when we put this -> that's will help us to have what we want as type after execution"""


def area(longueur: float, largeur: float) -> int:
    return longueur * largeur


# we have class float but the result is class integer
print(area.__annotations__)
# {'longueur': <class 'float'>, 'largeur': <class 'float'>, 'return': <class 'int'>}


def afficher(string: int) -> str:
    print(string)


# we have class integer but the result is class string
print(afficher.__annotations__)
# {'string': <class 'int'>, 'return': <class 'str'>}

afficher(3)
# ------------------------------------------------------------------------------------------------
"""verify statique type of the file with mypy"""

"""install mypy and IPython"""
# pip install IPython
# pip install Imypy

from IPython.core.magic import register_cell_magic


@register_cell_magic
def typecheck(line, cell):
    from IPython import get_ipython
    from mypy import api
    cell = '\n' + cell
    mypy_result = api.run(['-c', cell] + line.split())
    if mypy_result[0]: 
        print(mypy_result[0])
    if mypy_result[1]:  
        print(mypy_result[1])
    shell = get_ipython()
    shell.run_cell(cell)



%%typecheck

def function(L : list) -> list:
    L = L + ['2']
    return(L)
           
print(function(['1+1 =']))

%%typecheck

def double(a : int) -> int: 
    a = a*2
    return(a)

double(27.6)

# error: Argument 1 to "double" has incompatible type "float"; expected "int"
# Found 1 error in 1 file (checked 1 source file)
# Insérez votre code ici

%%typecheck

import numpy as np

vec = np.array([2,4,6])

double(vec)

# error: Name "double" is not defined
# Found 1 error in 1 file (checked 1 source file)
# ------------------------------------------------------------------------------------------------
"""we can use mypy in terminal"""
#  mypy Python/11-Lists.py   ##like that we can check if we have errors
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
"""Decorators"""
"""A decorator in Python can be seen as a function that modifies the behavior of other functions.
In general, you use decorators when you want to add some code to several functions, without having to modify them."""

def print_before_execution(function):
   def print_then_execute(*args, **kwargs):
       print('this is what the function {} returns'.format(function.__name__))
       function(*args, **kwargs)
   return print_then_execute

@print_before_execution
def print_hello_world():
    print("hello world")
print_hello_world()

# this is what the function print_hello_world returns
# hello world
# --------------------------------------------------------------------------------
# this function will print the file we want to open
def affiche_doc(function):
    def print_doc(*args, **kwargs):
        print(function.__doc__)
        return function(*args, **kwargs)
    return print_doc


import pandas as pd


# to print the file we apply the previous function and we apply the import function
@affiche_doc
def importer_csv(*args, **kwargs):
    '''
    Fonction qui permet d'importer un fichier csv dans un DataFrame pandas.
    '''
    return pd.read_csv(*args, **kwargs)

importer_csv('../03-Numpy_pandas_scikit/data/automobiles.csv')
# ------------------------------------------------------------------------------------------------
"""We often use decorators to display the execution time of a function without having to modify its code."""

import time


def execution_time(function):
    def timer(*args, **kwargs):
        heure_debut = time.time()
        results = function(*args, **kwargs)
        heure_fin = time.time()
        times = heure_fin - heure_debut
        print("This function was executed in {} s".format(times))
        return results
    return timer

@execution_time
def importer_csv(*args, **kwargs):
    '''
    Fonction qui permet d'importer un fichier csv dans un DataFrame pandas.
    '''
    return pd.read_csv(*args, **kwargs)

importer_csv('../03-Numpy_pandas_scikit/data/automobiles.csv')
# This function was executed in0.03759336471557617 s
# ------------------------------------------------------------------------------------------------
"""
**parameters of decorator**

- You can parameterize the behavior of a decorator in the same way as you parameterize that of a function.
- A parameterized decorator is actually a function that returns a simple decorator."""

def decorateur_parametre(description): 
    def decorateur(function): 
        def print_before_execution(*args, **kwargs): 
            print(description.format(function.__name__))
            function(*args, **kwargs)
        return print_before_execution
    return decorateur

@decorateur_parametre('this is what the function {} returns')
def print_hello_world():
    print('hello world')
print_hello_world()

# this is what the function print_hello_world returns 
# hello world
# --------------------------------------------------------------------------------
def entree_contient(a_contenir):
    def decorator(function): 
        def new_function(*args, **kwargs): 
            if a_contenir in str(args[0]):
                return function(*args, **kwargs)
            else:
                return "the first entry must contain {}".format(a_contenir)
        return new_function
    return decorator

@entree_contient('.csv')
def importer_csv(*args, **kwargs):
    '''
    Fonction qui permet d'importer un fichier csv dans un DataFrame pandas.
    '''
    return pd.read_csv(*args, **kwargs)

importer_csv('../03-Numpy_pandas_scikit/data/automobiles')
# 'the first entry must contain .csv'

# ------------------------------------------------------------------------------
"""
**Chain decorators**

- It is quite possible to assign several decorators to a function to accumulate their effects."""

def print_before_execution(function):
    def print_then_execute(*args, **kwargs):
        print('this is what the function {} returns'.format(function.__name__))
        function(*args, **kwargs)
    return print_then_execute

def print_after_execution(function):
    def execute_then_print(*args, **kwargs):
        function(*args, **kwargs)
        print('The function has finished running')
    return execute_then_print

@print_after_execution
@print_before_execution
def print_hello_world():
    print('hello world')

print_hello_world()


# this is what the function print_hello_world returns
# hello world
# # The function has finished running
# ------------------------------------------------------------------------------------------------
def entree_contient(a_contenir):
    def decorator(function): 
        def new_function(*args, **kwargs): 
            if a_contenir in str(args[0]):
                return function(*args, **kwargs)
            else:
                return "the first entry must contain {}".format(a_contenir)
        return new_function
    return decorator

@entree_contient('.csv')
@execution_time
def importer_csv(*args, **kwargs):
    '''
    Fonction qui permet d'importer un fichier csv dans un DataFrame pandas.
    '''
    return pd.read_csv(*args, **kwargs)

importer_csv('../03-Numpy_pandas_scikit/data/automobiles')
# 'the first entry must contain .csv'

importer_csv('../03-Numpy_pandas_scikit/data/automobiles.csv')
# This function was executed in 0.020455598831176758 s
# ------------------------------------------------------------------------------------------------
"""Wrap a function"""

def print_before_execution(function):
    def print_then_execute(*args, **kwargs):
        print('this is what the function {} returns'.format(function.__name__))
        function(*args, **kwargs)
    return print_then_execute

@print_before_execution
def print_hello_world():
    '''
    Description de ma fonction
    '''
    print("hello world")
    
help(print_hello_world)
# Help on function print_then_execute in module __main__:

# print_then_execute(*args, **kwargs)

"""To remedy this problem, we wrap our function to be decorated using wraps, which returns a decorator 
when called with a function. wraps is available in the functools library."""

from functools import wraps


def print_before_execution(function):
    @wraps(function)
    def print_then_execute(*args, **kwargs):
        print('this is what the function {} returns'.format(function.__name__))
        function(*args, **kwargs)
    return print_then_execute

@print_before_execution
def print_hello_world():
    '''
    Description de ma fonction
    '''
    print("hello world")
    
help(print_hello_world)

# Help on function print_hello_world in module __main__:

# print_hello_world()
#     Description de ma fonction


def factorial(n):
    if n==1:
        return(n)
    else:
        return(n*factorial(n-1))
    
@execution_time
def boucle(n=500):
    L=[]
    for k in range(1,n):
        L.append(factorial(k))
    return(L)

### Exécution         
boucle(500)


"""improve the performance of our code using the @lru_cache() decorator"""
from functools import lru_cache


@lru_cache()
def factorial(n):
    if n==1:
        return(n)
    else:
        return(n*factorial(n-1))

boucle(500)

"""sleep 5 seconds"""

@execution_time
@lru_cache()
def print_hello(a='hello'):
    time.sleep(5)
    return a

a = print_hello()
# This function was executed in 5.0085289478302 s

"""the calculated value remains stored in cache so we can execute it again and it take 0 seconds"""
b= print_hello()
# This function was executed in 0.0 s
# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------
"""Multithreading and multiprocessing"""

# pip install threaded

import time
from threading import Thread


# Fonction name 
def name():
    time.sleep(10)
    name1="Daniel"
    name2=input("Ecrivez le prénom Donna: ")
    print(name1,"&",name2)

# Fonction calcul 

def calcul(x):
    x=x**1000000
    print(int(str(x)[:2])) # On affiche les deux premiers chiffres seulement
    
# Exécution en séquentiel 

t1=time.time() # On démarre la mesure du temps

name()          # On exécute la fonction name

calcul(5)       # On exécute la fonction calcul

t2=time.time() # On arrête la mesure du temps

print("\nLa complétion du programme en séquentiel prend : ", t2-t1,"\n")

# Exécution en threads

th1=Thread(target=name) # Premier thread avec la fonction name 

th2=Thread(target=calcul,args=(5,)) # Deuxième thread avec la fonction calcul 

t1=time.time() # On démarre la mesure du temps

th1.start()      # On démarre le thread 1

th2.start()      # On démarre le thread 2

th1.join()       # On s'assure de la complétion du thread 1

th2.join()       # On s'assure de la complétion du thread 2

t2=time.time() # On arrête la mesure du temps

print("\nLa complétion du programme divisé en threads prend : ", t2-t1)



import time

import wikipedia

# On définit la langue de prédilection

wikipedia.set_lang("fr") 

# On définit une liste de titre de pages dont on souhaite obtenir le contenu

pages = ["Multithreading", "Threading", "Programmation_concurrente"]

# On définit une fonction qui retourne la première ligne de chaque page wikipédia 
# dont le nom apparaît dans la liste pages définit précédemment

def wikipedia_fonction(page):
    wiki = wikipedia.page(page)
    text = wiki.content
    print("\n",page,' : ',text.split('.', 1)[0],"\n")

t1=time.time() # On démarre la mesure du temps

# Lancement en séquentiel à l'aide d'une boucle

for page in pages:
    wikipedia_fonction(page) 

t2=time.time() # On arrête la mesure du temps

print (" \n Durée: ",(t2 - t1))



# Insérez votre code 
from threading import Thread

t1=time.time() # On demarre la mesure du temps

# On crée une liste de threads, le nombre de threads correspond au nombre de pages renseigné

threads = [Thread(target=wikipedia_fonction, args=(page,)) for page in pages] 

# On démarre les threads 

for thread in threads:
    thread.start()

# On s'assure de la complétion des threads

for thread in threads:
    thread.join()
    
t2=time.time() # On arrête la mesure du temps

print ("\n Durée:", (t2 - t1))

# Le temps d'exécution est fortement réduit ! 
# L'affichage des pages n'est pas dans le même ordre que décrit au sein de la liste pages
# On ne contrôle pas l'ordre de complétion des threads

import multiprocessing
import time
from multiprocessing import Pool

import numpy as np

# On définit la fonction calcul_lourd

def calcul_lourd(x): 
    resultat = 0
    for k in range(1, 50):
        resultat += x * np.power(x, 1 / k*np.power(k,3/2))
    return resultat

t1=time.time() # On démarre la mesure du temps

# On exécute la fonction pour différents arguments à la suite

calcul_lourd(range(1000000)) 
calcul_lourd(range(5000000))
calcul_lourd(range(4000000))
calcul_lourd(range(7000000))

t2=time.time() # On arrête la mesure du temps

print("La complétion du programme en séquentiel prend : ", t2-t1)

t1=time.time() # On démarre la mesure du temps

pool = Pool(4) # On crée les processus

# On répartit l'exécution entre les coeurs
resultat = pool.map(calcul_lourd,[range(1000000),range(5000000),range(4000000),range(7000000)]) 

t2=time.time() # On arrête la mesure du temps

print("\nLa complétion du programme en parallèle prend : ",t2-t1)

# On définit la fonction calcul_while

def calcul_while(x): 
       while x>0:
            x-=1

# On définit la liste d'arguments

nombres=[5000000,3000000,6000000,4000000,320000000,2000000, 50000000,10000000]

t1=time.time() # On démarre la mesure du temps

# On exécute en séquentiel

for nb in nombres:
    calcul_while(nb)

t2=time.time() # On arrête la mesure du temps

print("Durée en séquentiel : ",t2-t1)

# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
"""Fonctions asynchrones"""

# On importe la librairie asyncio et la librairie time

import asyncio
import time

# On crée notre première coroutine

async def exemple():  # On définit la coroutine avec async def

    print("Nous essayons les coroutines.")

# On appelle la coroutine de la même façon qu'une fonction standard

exemple()

# On appelle la coroutine

await exemple()

# Définition de la fonction nom qui en retour affiche le prénom donné en argument après 10 secondes d'attente

def nom(prenom):
    name = prenom
    time.sleep(10)
    print(name)

# Définition de la fonction main qui affiche le temps de complétion de l'exécution
# de la fonction nom pour trois arguments différents


def main():
    print("Subroutine :")
    start_time = time.time()
    nom('Daniel')
    nom('Donna')
    nom('Diane')
    end_time = time.time()
    print("Durée totale d'exécution: %.2f secondes" % (end_time - start_time))


main()

# Définition de la coroutine nom qui en retour affiche le prénom donné en argument après 10 secondes d'attente


async def nom_async(prenom):
    name = prenom
    await asyncio.sleep(10)
    print(name)

# Définition de la coroutine main qui affiche le temps de complétion de l'exécution
# de la fonction nom pour trois arguments différents


async def main():
    print("\nCoroutine :")
    start_time = time.time()
    await asyncio.gather(nom_async('Daniel'), nom_async('Donna'), nom_async('Diane'))
    end_time = time.time()
    print("Durée totale d'exécution: %.2f secondes" % (end_time - start_time))

await main()

# On constate que le temps d'exécution est divisé par trois.

# Définition de la fonction name qui en retour affiche le prénom Daniel

def name():
    name = "Daniel"
    time.sleep(10)
    print(name)

# Définition de la fonction calculation qui en retour affiche les deux premiers chiffres d'un calcul


def calculation(x):
    x = x**1000000
    y = int(str(x)[:2])
    print(y)

# Définition de la fonction main qui affiche le temps de complétion de l'exécution
# de la fonction name et de la fonction calculation pour deux arguments différents


def main():
    print("Subroutine :")
    start_time = time.time()
    name()
    calculation(5)
    calculation(3)
    end_time = time.time()
    print("Durée totale d'exécution: %.2f secondes" % (end_time - start_time))


main()

# Définition de la coroutine name_async qui en retour affiche le prénom Daniel


async def name_async():
    name = "Daniel"
    await asyncio.sleep(10)
    print(name)

# Définition de la coroutine calculation_async qui en retour affiche les deux premiers chiffres d'un calcul


async def calculation_async(x):
    x = x**1000000
    y = int(str(x)[:2])
    print(y)

# Définition de la fonction main qui affiche le temps de complétion de l'exécution
# de la fonction name_async et de la fonction calculation_async pour deux arguments différents
# On crée une tâche pour l'exécution de chaque fonction, cela permet de lancer l'exécution de façon concurrente


async def main():
    print("\nCoroutine :")
    start_time = time.time()
    task1 = asyncio.ensure_future(name_async())
    task2 = asyncio.ensure_future(calculation_async(5))
    task3 = asyncio.ensure_future(calculation_async(3))

    await task1
    await task2
    await task3

    end_time = time.time()
    print("Durée totale d'exécution: %.2f secondes" % (end_time - start_time))

await main()

# On constate que le temps d'exécution est divisé par deux.



# On importe la librairie wikipedia

import asyncio
import time

import wikipedia

# On définit la langue de prédilection

wikipedia.set_lang("fr")

# On définit une fonction qui retourne le résumé de chaque page et qui a des temps d'attente bloquants


def wiki(page):
    time.sleep(6)
    print('\n', wikipedia.summary(page))

# On définit une fonction main pour lancer la fonction avec différents arguments


def main():

    print("Subroutine :")

    start_time = time.time()  # On démarre la mesure du temps

    wiki("Coroutine")

    wiki("Threading")

    wiki("Programmation_concurrente")

    end_time = time.time()  # On arrête la mesure du temps

    print("\nDurée totale d'exécution: %.2f secondes" %
          (end_time - start_time))

# On appelle la fonction main


main()



import asyncio
import time

import wikipedia

wikipedia.set_lang("fr")

async def wiki_async(page):
    await asyncio.sleep(6)
    print('\n', wikipedia.summary(page))

# On définit la coroutine main pour lancer les coroutines simultanément grâce à la coroutine gather


async def main():

    print("Coroutine :")

    start_time = time.time()  # On démarre la mesure du temps

    await asyncio.gather(wiki_async("Coroutine"), wiki_async("Threading"), wiki_async("Programmation_concurrente"))

    end_time = time.time()  # On arrête la mesure du temps

    print("\nDurée totale d'exécution: %.2f secondes" %
          (end_time - start_time))

# On appelle la coroutine main

await main()

# On constate bien un gain de temps substantiel entre les deux méthodes.
