points = 174  # use this as input for your submission

# establish the default prize value to None
prize = None

# use the points value to assign prizes to the correct prize names
if points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
    prize = "wooden rabbit"
elif points <= 150:
    result = "Oh dear, no prize this time."
    prize == None
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
    prize = "Wafer-thin mint"
else:
    result = "Congratulations! You won a penguin!"
    prize = "Penguin"
# use the truth value of prize to assign result to the correct prize
if prize == None:
    result = "Oh dear, no prize this time."
else:
    print("Congratulations! You won a {}!".format(prize))

print(result)
