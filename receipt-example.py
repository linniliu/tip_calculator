
shopping_list = [123, 123, 444, 432, 221, 444]

counts ={123 :2, 444 :2, 432 :1, 221 :1}

store_inventory = {123: ("Tea", 4.99), 444: ("Coffee", 16.99), 432: ("Juice", 3.99), 221: ("Aero Bar", 1.19)}



# (1) Print out a list of what was purchased.
# (2) Print out the total price.

# Loop through the shopping list.
#  For each item in the shopping list, look up the record in store inventory.
#  Print out the items in a nice format.
#  Before moving on, capture the cost of this item.
#  At the end display the cost.

total_cost = 0.00

print("RECEIPT")
print("=" * 20)

for i in shopping_list:
    item_name, item_price = store_inventory[i]
    print("{0:20s}${1:.2f}".format(item_name, item_price))
    total_cost += item_price

print("\nTOTAL: ${:.2f}".format(total_cost))