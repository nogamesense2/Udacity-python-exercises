tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for i in range(len(tokens)):
    if tokens[i][0] == '<' and tokens[i][-1] == '>':
        count += 1

print(count)
