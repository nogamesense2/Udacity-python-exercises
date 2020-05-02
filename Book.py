book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}
# **Step 2.** Iterate through each element in the list. If an element is already included in the dictionary, add 1 to its value. If not, add the element to the dictionary and set its value to 1.
for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1
print(word_counter)
