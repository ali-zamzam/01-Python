"""Strings"""

"""String methods"""

# s.capitalize()Capitalize s # 'hello' => 'Hello'
# s.lower()Lowercase s # 'HELLO' => 'hello'
# s.swapcase()Swap cases of all characters in s # 'Hello' => "hELLO"
# s.title()Titlecase s # 'hello world' => 'Hello World'
# s.upper()Uppercase s # 'hello' => 'HELLO'
# Sequence Operations I
# s2 in sReturn true if s contains s2
# s + s2Concat s and s2
# len(s)Length of s
# min(s)Smallest character of s
# max(s)Largest character of s
# Sequence Operations II
# s2 not in sReturn true if s does not contain s2
# s * integerReturn integer copies of s concatenated # 'hello' => 'hellohellohello'
# s[index]Character at index of s
# s[i:j:k]Slice of s from i to j with step k
# s.count(s2)Count of s2 in s
# Whitespace I
# s.center(width)Center s with blank padding of width # 'hi' => ' hi '
# s.isspace()Return true if s only contains whitespace characters
# s.ljust(width)Left justifiy s with total size of width # 'hello' => 'hello '
# s.rjust(width)Right justify s with total size of width # 'hello' => ' hello'
# s.strip()Remove leading and trailing whitespace from s # ' hello ' => 'hello'
# Find / Replace I
# s.index(s2, i, j)Index of first occurrence of s2 in s after index i and before index j
# s.find(s2)Find and return lowest index of s2 in s
# s.index(s2)Return lowest index of s2 in s (but raise ValueError if not found)
# s.replace(s2, s3)Replace s2 with s3 in s
# s.replace(s2, s3, count)Replace s2 with s3 in s at most count times
# s.rfind(s2)Return highest index of s2 in s
# s.rindex(s2)Return highest index of s2 in s (raise ValueError if not found)
# Cases II
# s.casefold()Casefold s (aggressive lowercasing for caseless matching) # 'ßorat' => 'ssorat'
# s.islower()Return true if s is lowercase
# s.istitle()Return true if s is titlecased # 'Hello World' => true
# s.isupper()Return true if s is uppercase
# Inspection I
# s.endswith(s2)Return true if s ends with s2
# s.isalnum()Return true if s is alphanumeric
# s.isalpha()Return true if s is alphabetic
# s.isdecimal()Return true if s is decimal
# s.isnumeric()Return true if s is numeric
# s.startswith(s2)Return true is s starts with s2
# Splitting I
# s.join('123')Return s joined by iterable '123' # 'hello' => '1hello2hello3'
# s.partition(sep)Partition string at sep and return 3-tuple with part before, the sep itself, and part after # 'hello' => ('he', 'l', 'lo')
# s.rpartition(sep)Partition string at last occurrence of sep, return 3-tuple with part before, the sep, and part after # 'hello' => ('hel', 'l', 'o')
# s.rsplit(sep, maxsplit)Return list of s split by sep with rightmost maxsplits performed
# s.split(sep, maxsplit)Return list of s split by sep with leftmost maxsplits performed
# s.splitlines()Return a list of lines in s # 'hello\nworld' => ['hello', 'world']
# Inspection II
# s[i:j]Slice of s from i to j
# s.endswith((s1, s2, s3))Return true if s ends with any of string tuple s1, s2, and s3
# s.isdigit()Return true if s is digit
# s.isidentifier()Return true if s is a valid identifier
# s.isprintable()Return true is s is printable
# Whitespace II
# s.center(width, pad)Center s with padding pad of width # 'hi' => 'padpadhipadpad'
# s.expandtabs(integer)Replace all tabs with spaces of tabsize integer # 'hello\tworld' => 'hello world'
# s.lstrip()Remove leading whitespace from s # ' hello ' => 'hello '
# s.rstrip()Remove trailing whitespace from s # ' hello ' => ' hello'
# s.zfill(width)Left fill s with ASCII '0' digits with total length width # '42' => '00042'

# {} accolades (Curly braces)
# [] crochets (Brackets)
# () parantheses
# " " doubles quotes
# ' ' simple quotes


# ---------------------------------------------------------------------------
message = '     Learn Python  '

# remove leading and trailing whitespaces
print('Message:', message.strip())           #output: Message: Learn Python

# ---------------------------------------------------------------------------
print("Hello Ali!")

# the output is HelloAli
print("Hello" + "Ali")

# variable 1
hello = "Hi"

# variable 2 
Name1 = "Ali"

# we put (+ ' ' +) to have a space between the tow variables.
print( hello + ' ' + Name1)

# or
print(hello,Name1)


# We can use input 
Name  = input("Can you please enter your Name: ")

# with no space
print("hello" + Name)

# with space
print("hello" + ' ' + Name)


# usually we use str(number) if we want to print a number with a string
age1 =24

# print("my age is " + age) # error so we need to do this
print("my age is " + str(age1)) # when we put the str(age) --> all good

#----------------------------------------------------------------------------------------
"""String-indexing"""

# we use this  methode ([]) to print what we want from string
# result (p) # the first letter is (0) the second is (1)
word = 'python'
print(word[0])   


word = 'python'     # if we want the last letter of string we put [-1]
print(word[-1])     # resultat (n)


word = 'python'
print(word[0:3])  # resultat (pyt)

# if we want the whole word with the method of string indexing
# we can put [0:]
print(word[0:])  # resultat (python)


#if we have a phrase and there's a many words seperated by (,) the methode choose word by word (not letter by letter)
phrase1 = "python", "java", "c#"

print(phrase1[1])  # result (java)

phrase2 = "python",30, "java", "c#"

print(phrase2[1])  # result (30)


# to have the letter in word in the phrase we use
phrase3 = "python", "java", "c#"
print(phrase3[0][1])  # result (y)

#----------------------------------------------------------------------------------------
"""Formatted string literal or f-string"""

# A formatted string literal or f-string is a string literal that is prefixed with 'f' or 'F'.
# These strings may contain replacement fields, which are expressions delimited by curly braces {}.
# While other string literals always have a constant value, formatted strings are really expressions evaluated 
# at run time.

match_df = ["one", "two", "three", "four", "five", "six"]

print(f"There are {len(match_df)} matched needs with available and Engaged ressources")

name = "Fred"
print(f"He said his name is {name}.")           # output = "He said his name is Fred."

name = "Fred"
print(f"He said his name is {name!r}.")         # output = "He said his name is 'Fred'."

# repr() is equivalent to !r  
print(f"He said his name is {repr(name)}.")     # "He said his name is 'Fred'."

print("my age is {0}".format(29))



age2 = 30
print("my age is {0}".format(age2))

# if we have multible int and we need to put it

print("there is {0} days in {1},{2},{3},{4},{5}".format(31,"jan","mar","may","jul","aug"))

print("there is {0} days in february and {1} in april and {2} in march".format(28,30,31))
# {0} = 28 , {1} = 30, {2} = 31


# or using f befor the string and put the int in the {}.
age3 = 31
print(f"my age is {age3}")

Name = "Ali"
age3 = 30
print(Name + f" is {age3} years old")

a,b,c = 28,30,31
print(f"there is {a} days in february and {b} in april and {c} in march")


for i in range(1,11):
    print("the first number is {0} and the squared is {1} and the cube is {2}".format(i,i**2,i**3))
    # {0} = i, {1} =i**2 , {2} = i**3


# f is floating point format (7 digits by default)
# decimals (50digits by default)

print("Pi is approximatley to {0:12f}".format(22/7))  # {0: } the number after 0: is the width (how much digits)

# when we put after 0: a number with . like that (12.20) thats mean we want to have more the 7 digits and more than 12
# the programme will print 20 digits after the point
print("Pi is approximatley to {0:12.20f}".format(22/7))

# when we put after 0: a number with . like that (62.50) thats mean we want to have more than 50 digits
# but by default we have 50 digits in decimal so we saw a space in the result
print("Pi is approximatley to {0:62.50f}".format(22/7))

# when we put < after 0: thats mean we want to have digits with no space
print("Pi is approximatley to {0:<72.50f}".format(22/7))

# ------------------------------------------------------------------------
# if we want to use this with the f-string method

print(f"Pi is approximatley to {22/7:<72.50f}")

#----------------------------------------------------------------------------------------
"""Escape Characters in Strings"""

split_string="this is:\nthe first code\ni did it"
#output = this is:      
# the first code
# i did it 
print(split_string)


tabbed_string="1\t2\t3\t"
print(tabbed_string)   # output = 1       2       3

#For write a ' in the string we use \

print("there\'s another solution")
print("""it's my second "solution"  """)


# slicing
parrot = "Norwegian Blue"

print(parrot[0:6])
print(parrot[3:6])
print(parrot[2:])
print(parrot[-4:-2])
# ------------------------------------------------------------------
# Using a step in slicing

print(parrot[2:12:2])  # reinB

# Using a backward step in slicing
print(parrot[12:2:-2])  # uBnie


# ------------------------------------------------------------------------------
