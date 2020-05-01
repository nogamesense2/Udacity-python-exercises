given_name = "William"
middle_name = "Bradley"
family_name = "Pitt"

name_length = len(given_name + middle_name + family_name)

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)
