# ITP Week 1 Day 2 Exercise

# Take an user's input for his age
age = input("Enter your age: ")

# The user input comes in as a string so we have to cast it to a int!
if(age.isnumeric()):   # test that input string has only 'numbers'.  This also handles negative values.
    age = int(age)
else:
    print("You entered an invalid age.  Please try again.")
    exit()

# Use an if/else to determine if they are of legal drinking age.
# if the user is of age, print "Welcome!"
# else, tell them to come back in X amount of years (use math operations)
legal_drinking_age = 21
if(age >= legal_drinking_age):
    print("Welcome, drink up!")
else:
    years = legal_drinking_age - age
    print("You're too young for a drink.   Please come back in " + str(years) + " years, young buck!")

# Bonus: Add a validation by checking the type of the user input
# to ensure it can be casted as an int. Handle any other input that
# are not numbers to try again.

#####  SEE bonus code attempt above. ~Darren ######
