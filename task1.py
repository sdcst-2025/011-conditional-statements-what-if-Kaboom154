#! python3

"""
Have the user input a number. 
Determine if the number is larger than 100 
If it is, the output should read "The number is larger than 100" 
(2 points)
Inputs:
number
Outputs:
"The number is larger than 100"
"The number is smaller than 100"
"The number is 100"

Example:
Enter a number: 100
The number is 100

Enter a number: 102
The number is larger than 100
"""

def greaterThan100(num):
    if num > 100:
        return "the number is larger than 100"
    if num < 100:
        return "the number is smaller than 100"
    if num == 100:
        return "the number is 100"

x = float(input("number: "))
print(
    greaterThan100(x)
)