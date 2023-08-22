# Write a Python script that takes multiple strings assigns the concatenation of all the strings to a variable using the "+=" operator. Print the value of the variable.

# - Your result should look like this:

# ```
# The concatenated string is: applebananacherry
# ```



str1 = "apple"
str2 = "banana"
str3 = "cherry"

concatenated = ""
concatenated += str1
concatenated += str2
concatenated += str3

print("The concatenated string is:", concatenated)
