import math

#Explain to user the use of this program.
print("This program is designed to help you caluclate the number of")
print("boxes needed for how many items you need shipped.")

print()

#Ask user for number of items they wish to ship.
user_items = int(input("Please enter the number of items you wish to ship: "))

#Ask user for number of items they wish to have in each box.
items_per_box = int(input("Please enter the number of items you wish to ship per box: "))

print()

#Develop a math formula to calculate the number of boxes needed to ship the items,
#the user has provided.
boxes_needed = math.ceil(user_items / items_per_box)

print(f"For {user_items} items, packing {items_per_box} items in each box,")
print(f"you will need {boxes_needed} boxes.")