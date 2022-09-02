"""split and join"""

"""split transform the string to a list"""
string = "yes-No"

new = string.split("-")
print(new)
# output : ['yes', 'No']


"""join transform the list to a string"""
joined2 = " or ".join(new)

print(joined2)
print(type(joined2))

# ----------------------------------------------------------------
result = "CBU-15-EES-Developpement & digital"

# here the split will transform the string to a list so we can use the list slice
# [],to have what we want from the string
new = result.split("-")[0]
print(new)
# output = CBU


text = "CBU-15-EES-Developpement & digital"


def cbu(result):

    new = result.split("-")[1]
    return new


print(cbu(text))

# output = 15


def cbu_name(cbu):

    new = cbu.split("-")[2]
    return new


print(cbu_name(text))


# input string
s = "Geeks-Geeks"

new = s.split("-")
print(new)

joined = " ".join(new)

print(joined)

joined2 = " and ".join(new)

print(joined2)
print(type(joined2))

# ----------------------------------------------------------------
""" strip will remouve the space """
str1 = " Geeks-Geeks "

result = str1.strip()

print(result)
print(type(result))
