# Python Program to Add Two Matrices
# Program to add two matrices using nested loop
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]
for r in result:
   print(r)
# [17, 15, 4]
# [10, 12, 9]
# [11, 13, 18]

# Source Code: Matrix Addition using Nested List Comprehension
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]
result = [[x[i][j]+y[i][j] for j in range(len(x[0]))] for i in range(len(x))]
for r in result:
    print(r)

# Python Program to Create Pyramid Patterns
# *
# * *
# * * *
# * * * *
# * * * * *
rows = int(input("Enter number of rows: "))
for i in range(rows):
  for j in range(i+1):
    print("*", end="")
  print()

# Python Program to Display Fibonacci Sequence Using Recursion
# Python program to display the Fibonacci sequence
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
nterms = 10
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
# Fibonacci sequence:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34

# Python Program to Find Sum of Natural Numbers Using Recursion
def sum(n):
  if n<=1:
    return n
  else
    return n + sum(n-1)
num = 16
if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",recur_sum(num))
# The sum is 136

# Python Program to Convert Decimal to Binary Using Recursion
def converttobinary(n):
  if n > 1:
    converttobinary(n//2)
  print(n%2, end = '')
dec = 34
converttobinary(dec)
print()
# 100010
