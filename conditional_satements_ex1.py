points = 174  # use this input to make your submission

# write your if statement here
if points > 181:
    result = "penguin"
elif points > 151 and points < 181:
    result = "wafer-thin mint"
elif points > 51 and points < 151:
    result = "no prize"
else:
    result = "wooden rabbit"

print(result)
