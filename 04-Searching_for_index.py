"""searching index with for loop"""

shopping_list = ["milk","egg","spam","pasta"]

item_to_found = "spam"

found_at = None

for index in range (len(shopping_list)):
    if shopping_list[index] == item_to_found:
        found_at=index
        break             # because we found what we search so no need to continue the loop
print(f"item found at the {found_at} position.")

print("-"*20)
# -----------------------------------------------------------------
# or

shopping_list = ["milk","egg","spam","water"]

item_to_found = "pasta"

found_at = None

if item_to_found in shopping_list:
    found_at = shopping_list.index(item_to_found)
    print(f"item found at the {found_at} position.")

if found_at is not None:
    print(f"item found at position {found_at}")
else:
    print(f"{item_to_found} not found ")
