# ITP Week 1 Day 4 Exercise


# Dictionary Loop

inventory = {
    "soda_cans": 45,
    "chips": 12,
    "sandwiches": 34,
    "candy": 1
}

# SCENARIO: A person came in and bought one of everything!

for item in inventory.items():
    # decrement item by using an assignment operator (Day 2 Lecture line #130)
    inventory.update({item[0]: item[1] + 1})
    # NOTE: recall that item represents the key of the key:value pair
print(inventory) #print changes after increment of values

# SCENARIO: REMOVE ANY 0 ITEMS

del_list = []j   #create empty list
for item in inventory.items():
    # use an if statement to check if the value is 0 and then remove it
    if(item[1] == 0):
        del_list.append(item[0])  #build list of keys that need to be deleted

for k in del_list:        #loop through list of items to be deleted, by key
    del inventory[k]      #delete item based on current k

print(inventory)          #print inventory to show if any items where deleted.

