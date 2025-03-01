# ITP Week 1 Day 4 Exercise


# Dictionary Loop

inventory = {
    "soda_cans": 45,
    "chips": 12,
    "sandwiches": 34,
    "candy": 1
}

#print out original dictionary before we modify it.
print()
print("original dictionary:")
print("\t", inventory)
print()


# SCENARIO: A person came in and bought one of everything!

#loop through dictionary and decrement count of each item by 1.
for item in inventory:
    # decrement item by using an assignment operator (Day 2 Lecture line #130)
    inventory.update({item : inventory[item]-1})
    # NOTE: recall that item represents the key of the key:value pair


#print dictionary after running increment to values. 
#all item values should be increased by 1.
print("dictionary after item values have been incremented by 1:")
print("\t", inventory) 
print()



# SCENARIO: REMOVE ANY 0 ITEMS

#adding some "zero" items for removal (plus some others)
inventory["slushee"] = 0
inventory["hotdogs"] = 3
inventory["donuts"] = 0
inventory["nachos"] = 8

#print current dictionary
print("\ndictionary with extra items added:")
print("\t", inventory)
print()


del_list = []   #create empty list of items to be deleted from inventory dictionary
for item in inventory:
    # use an if statement to check if the value is 0, in order to mark it for removal
    if inventory[item] == 0:
        del_list.append(item)  #build list of items that need to be deleted

for item in del_list:        #loop through list of items to be deleted
    del inventory[item]      

print("dictionary after *zero* items have been removed.")
print("\t", inventory)          #print inventory to show if any items where deleted.
print()
