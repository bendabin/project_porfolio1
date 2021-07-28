import re
"""
Write a regular expression that matches the word "Dutch" in the Zen of Python
"""
with open("zen_of_python.txt", "r") as zen_file:
    zen_str = zen_file.read()                           #Save contents of file into a string variable

word = "Dutch"                                          #Regular Expression input word
matches = re.findall(word, zen_str,re.IGNORECASE)
print(matches)                                          #Print the result


#Regular Expression for finding digits in string
reg_string = "Arizona 479, 501, 870. California 209, 213, 650."



matches2 = re.findall('[0-9]+', reg_string)


#matches2 = re.findall("\d",reg_string, re.IGNORECASE)
print(matches2)
