tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for i in range(len(tokens)):
    if '<' and '>' in  tokens[i]:
        count += 1

print(count)
