# Worksheet 1.2: Task 1 Solution

import sys

grade = input("enter a grade between 0-100: ")

if not grade.isdecimal():
    sys.exit("Error: Grade must be an integer between 0 and 100")

grade1 = int(grade)


if grade1 < 0 or grade1 > 100:
    sys.exit("Error: Grade must be an integer between 0 and 100")
    

elif grade1 <= 39:
    print(f"{grade1} is a Fail")
    

elif grade1 <70 :
    print(f"{grade1} is a Pass")
    
else:
    print(f"{grade1} is a Distinction")
    