# Program to display calendar of the given month and year
import calendar
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))
print(calendar.month(yy, mm))
# output
#    November 2014
# Mo Tu We Th Fr Sa Su
#              1  2
# 3  4  5  6 7  8  9
# 10 11 12 13 14 15 16
# 17 18 19 20 21 22 23
# 24 25 26 27 28 29 30


# Example 1: Using pathlib.Path.mkdir
from pathlib import Path
Path("/root/dirA/dirB").mkdir(parents=True, exist_ok=True)

# Example 2: Using os.makedirs
import os
os.makedirs("/root/dirA/dirB")

import random 
print(random.randint(0,9))  #random.randint(a,b)

import cmath
a = 1
b = 5
c = 6
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(sol1,sol2))
# The solutions are (-3+0j) and (-2+0j)

import cmath  
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    return [root1, root2]
    

# Example 3: Using distutils.dir_util
import distutils.dir_util
distutils.dir_util.mkpath("/root/dirA/dirB")

# Example 4: Raising an exception if directory already exists
import os
try:
    os.makedirs("/dirA/dirB")
except FileExistsError:
    print("File already exists")

import random
print(random.randint(1,10))
