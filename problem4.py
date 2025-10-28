#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# has a percent difference less than 2%
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
"""
Example:
Enter one side: 5
Enter a second side: 13
Enter third side: 12
that is a right triangle

Enter one side: 13.01
Enter a second side: 5
Enter third side: 12
that is a right triangle

Enter one side: 5
Enter a second side: 15
Enter third side: 12
that is an obtuse triangle
"""

a = float(input("enter a number: "))
b = float(input("enter another number: "))
c = float(input("enter another number: "))
sides = [a,b,c]
sides.sort()

a2 = (sides[2]**2)*0.98
b2 = (sides[2]**2)*1.02

if a2 < ( sides[0]**2 + sides[1]**2 ) < b2: # check for right triangle w/ pythagoreas
    print("that is a right triangle")
elif b2 >= ( sides[0]**2 + sides[1]**2 ):
    print("that is an obtuse triangle")
elif a2 <= ( sides[0]**2 + sides[1]**2 ):
    print("that is an acute triangle")
