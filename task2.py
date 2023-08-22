
# Write a Python script that takes multiple integers and assigns the product of all the numbers to a variable using the "*=" operator. Print the value of the variable.

# - Your result should look like this:

# ```
# The product is: 120


# I use int to make integer
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))
num4 = int(input("Enter the fourth integer: "))


# first, product is equal to 1, then we enter num1=2, num2=3, num3=4, num4=5 then we have 120 
product = 1
product *= num1
product *= num2
product *= num3
product *= num4

# Print the result
print("The product is:", product)