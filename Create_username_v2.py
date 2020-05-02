usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for i in range(len(usernames)):
    usernames[i] = usernames[i].lower()
    usernames[i] = usernames[i].replace(' ','_')

print(usernames)
