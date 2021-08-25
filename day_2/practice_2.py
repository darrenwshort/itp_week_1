# This is a number magic trick
# Pick a number from 1 - 9
# Multiply by 2
# Add 10 to the total
# Divide by 2
# Subtract by the original number
# Final number is 5

# Take an user's input
# Assign a new variable for each step
# at the end, use an if statement to see if the final is always 5!

print()
user_input = int(input("Enter number from 1 - 9: "))

# test if non-int, eg: str
if(not isinstance(user_input, int)):
    print("You must enter an integer value from 1 - 9.")
    exit()

# test range
if(user_input < 1 or user_input > 9):
    print("You must enter a number from 1 - 9 only.  Please restart program.")
    exit()


multiplied = user_input * 2
added = multiplied + 10
divided = added / 2
final_num = divided - user_input

# test final # is indeed 5
if(final_num == 5):
    print("Final number is 5.  You did it!")
else:
    print("Final number was something other than 5.  Please try again.")

print()



