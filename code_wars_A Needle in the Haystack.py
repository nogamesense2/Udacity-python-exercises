def find_needle(haystack):
    # your code here
    for i in range(len(haystack)):
        if haystack[i] == "needle":
           return ("found the needle at position {}".format(i))
