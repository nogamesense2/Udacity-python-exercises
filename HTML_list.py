items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here
for i in range(len(items)):
    html_str = html_str + "<li>" + items[i] + "</li>\n"
    html_str = html_str + "</ul>"

print(html_str)
