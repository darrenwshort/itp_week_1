# ITP Week 1 Day 4 (In-Class) Practice

# Dictionary

person_1 = {
    "first_name": "Scooby",
    "favorite_snack": "Rare Candy",
    "wears_glasses": True
    }

print(person_1) #print to see what are current contents


# verify the type of person_1 to be a dictionary by using type
print(type(person_1))

# add a key value pair to person_1 with the last_name of Doo
person_1["last_name"] = "Doo"

print(person_1) #print dict to see addition of last name

# update person_1 favorite_snack to "Scooby Snacks"
person_1.update({"favorite_snack": "Scooby Snacks"})

print(person_1) #print dict to see update to favorite snack

# Remove the "wears_glasses" key:value from person_1
del person_1["wears_glasses"]

print(person_1) #print to see deletion of wears_glasses


