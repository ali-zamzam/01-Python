
# Tuples are a data structure similar to lists() A very important nuance of tuples is that they are not modifiable).

un_tuple = "Bonjour", -1, 133
print(un_tuple)

# Tuple assignment
x, y, z = un_tuple

print(x)
print(y)
print(z)



"""Variables x, y and z were created and simultaneously assigned values. For the assignment tuple to work correctly, 
there must be as many variables to assign as there are elements in the tuple.

The tuple assignment gives an elegant syntactic solution to the value swapping problem: 
We have two variables a and b and we want to swap their values, i.e. a should take the value of b and b the value of has."""


# # Store the value of a in a temporary variable
# tmp = a

# # We update a with the value of b
# a = b

# # We update b with the value of the temporary variableb = tmp
# tmp = b

# # Thanks to the tuple assignment, this operation can be done in one line:
# # Échange de valeurs entre a et b
# a, b = b, a

a = 10
b = 5

a, b = b, a

print(a)
print(b)





