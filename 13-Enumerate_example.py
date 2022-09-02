# """ Getting the index in a loop with enumerate() """


# for index, character  in enumerate("abcdefgh"):
#     print(index+1,character)
# output
# 0 a
# 1 b
# 2 c
# 3 d
# 4 e
# 5 f
# 6 g
# 7 h

# or

# for index, character  in enumerate("abcdefgh"):
#     print(index+1,character)                      # we put +1 to start the index from 1 ( index start from 0 by default)
# output
# 1 a
# 2 b
# 3 c
# 4 d
# 5 e
# 6 f
# 7 g
# 8 h
# # ----------------------------------------------------------------
# # It is sometimes useful to have access to the index of an element in a sequence. To do this,
# #  it is possible to use the enumerate function in the for loop clause:

# furniture = ['table', 'chair', 'rack', 'shelf']

# for index, item in enumerate(furniture):
#     print(f'index: {index} - item: {item}')
# # index: 0 - item: table
# # index: 1 - item: chair
# # index: 2 - item: rack
# # index: 3 - item: shelf


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


# -------------------------------------------------------
names = ["neil armstrong", "buzz aldrin", "sally ride", "yuri gagarin", "elon musk"]


# Multiple positional Arguments - POSITION IS IMPORTANT
def custom_welcome_to_ship(name, space_ship):
    print(f"Welcome {name} to the {space_ship}")


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
