# Find square root of real or complex numbers
import cmath
num = 1+2j
num = eval(input('Enter a number: '))
num_sqrt = cmath.sqrt(num)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))

# Python Program to find the area of triangle
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)

# 2 practice
def area_of_triangle(base, height):
    area = 0.5 * base * height
    return round(area, 2)
base = 3
height = 4
print(area_of_triangle(base, height))

# Python Program to Find Armstrong Number in an Interval
# Program to check Armstrong numbers in a certain interval
lower = 100
upper = 2000
for num in range(lower, upper + 1):
   order = len(str(num))
   # initialize sum
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
   if num == sum:
       print(num)
# #output
# 153
# 370
# 371
# 407
# 1634

while True:
  n1 = int(input("enter: "))
  n2 = int(input("enter: "))
  print(n1 + n2)

# Python Program to Display the multiplication Table
num = int(input("Display multiplication table of? "))
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)
# output
# 12 x 1 = 12
# 12 x 2 = 24
# 12 x 3 = 36
# 12 x 4 = 48
# 12 x 5 = 60
# 12 x 6 = 72
# 12 x 7 = 84
# 12 x 8 = 96
# 12 x 9 = 108
# 12 x 10 = 120

# Python Program to Find HCF or GCD
def compute_hcf(x,y):
  if x>y:
    smaller = y
  else:
    smaller = x
  for i in range(1, smaller+1):
    if((x%i==0) and (y%i==0)):
      hcf = i
      return hcf
num1 = 54
num2 = 24
print("the h.c.f. is", compute_hcf(num1, num2))
# output
# The H.C.F. is 6

# Source Code: Using the Euclidean Algorithm
def compute_hcf(x,y):
  while(y):
    x,y = x&y`
  return x
hcf = compute_hcf(300, 400)
print("the hcf is", hcf)
# The HCF is 100

# Python Program to Merge Two Dictionaries
d1 = {1:'a', 2:'b'}
d2 = {2:'c', 4:'d'}
print(d1|d2)
# {1: 'a', 2: 'c', 4: 'd'}
