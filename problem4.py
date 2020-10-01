#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# It is close enough if the expected length of the hypotenuse and the actual length 
# differ by no more than 2% 
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
import math

a = float(input("Enter side A\n"))
b = float(input("Enter side B\n"))
c = float(input("Enter side C\n"))
if a > b and a > c:
    C = a
    B = b
    A = c
if b > a and b > c:
    C = b
    B = a
    A = c
if c > b and c > a:
    C = c
    B = b
    A = a
print(A , B , C)
#Right triangle
s = 100 * ((math.sqrt(A**2 + B**2))/C)
if int(s) in range (98,102):
    print("that is a right triangle")
#Obtuse triangle

#Acute triangle
