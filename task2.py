#! python3
"""
 Have the user input a number 
 Determine if the number is positive, negative or 0 
 2 points

 Inputs:
 number

 Outputs:
 - "positive"
 - "negative"
 - "zero"

 Example:

Enter a number: 3
positive

Enter a number: -1.2
negative
"""

def posNeg(num):
    if num > 0:
        return "positive"
    if num < 0:
        return "negative"
    if num == 0:
        return "zero"

x = float(input("number: "))
print(posNeg(x))