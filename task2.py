#! python3
# Have the user input a number 
# Determine if the number is positive, negative or 0 
# 2 points

# Inputs:
# number

# Outputs:
# - "positive"
# - "negative"
# - "zero"

n = int(input("Enter number\n"))
if n > 0:
    print("positive")
elif n < 0:
    print("negative")
elif n == 0:
    print("zero")