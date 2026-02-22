# Python Program to Count the Number of Each Vowel
# Program to count the number of each vowels
vowels = 'aeiou'
ip_str = 'Hello, have you tried our tutorial section yet?
ip_str = ip_str.casefold()
count = {}.fromkeys(vowels,0)
for char in ip_str:
   if char in
      count[char] += 1
print(count)
# output
# {'a': 2, 'e': 5, 'i': 3, 'o': 5, 'u': 3}

# Write a function to return the first N vowels from a given string.
# Return the first N vowels from the string. If there are fewer than N vowels in the string, return "Not found".
# For example, for input "Hello World", the output should be 'e', 'o', 'o'.

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
for i in range(rows):
  for j in range(i + 1);
    print(j + 1, end = " ")
  print()

# A
# B B
# C C C
# D D D D
# E E E E E
rows = int(input("Enter number of rows: "))
ascii_value = 65
for i in range(rows):
  for j in range(i+1):
    alphabet = chr(ascii_value)
    print(alphabet, end=" ")
  ascii_value += 1
  print()

# Programs to print inverted half pyramid using * and numbers
# Example 4: Inverted half pyramid using *
# * * * * *
# * * * *
# * * *
# * *
# *
input = int(input("Enter")
for i in range(input, 0, -1)
  for j in range(0, i):
    print("* ", end = " ")

  print()

# Programs to print full pyramids
# Example 6: Program to print full pyramid using *
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
rows = int(input("enter: "))
k = 0
for i in range(1, rows+1):
  for space in range(1, (rows-1) + 1):
    print(end = "  ")
  while k!=(2*i-1):
    print("* ", end = "")
    k+=1
  k = 0
  print()

# Example 8: Inverted full pyramid of *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *
rows = int(input("Enter number of rows: "))
for i in range(rows, 1, -1):
    for space in range(0, rows-i):
        print("  ", end="")
    for j in range(i, 2*i-1):
        print("* ", end="")
    for j in range(1, i-1):
        print("* ", end="")
    print()

 #           1
 #         1   1
 #       1   2   1
 #     1   3   3    1
 #   1  4    6   4   1
 # 1  5   10   10  5   1

rows = int(input("enter :")
coef = 1
for i in range(1, rows+1):
 for space in range(1, rows-i+1):
  print(" ", end = "")
 for j in range(0, i):
  if j == 0 or i ==0:
   coef = 1
  else:
   coef = coef * (i - j)//j
  print(coef, end = " ")
 print()
 
# Example 2: Using the ** Operator
d1 = {1: 'a', 2: 'b'}
d2 = {2: 'c', 4: 'd'}
print({**d1, **d2})
# {1: 'a', 2: 'c', 4: 'd'}
    

# Write a function to merge two dictionaries.
# Return the merged dictionary.
# For example, for inputs {'a': 1, 'b': 2} and {'c': 3, 'd': 4}, the output should be {'a': 1, 'b': 2, 'c': 3, 'd': 4}.
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = merge_dictionaries(dict1, dict2)
print(merged)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Example 5: Inverted half pyramid using numbers
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
rows = int(input("enter number of rows:"))
for i in range(rows, 0, -1):
  for j in range(1, i+1):
    print(j, end=" ")

  print()
  

# Python Program to Check Whether a String is Palindrome or Not
my_str='aIbohPhoBiA'
my_str = my_str.casefold()
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
  print("the string is a palindrom.")
else:
  print("the string is not a palindrome")
# The string is a palindrome.


# Example 10: Floyd's Triangle
# 1
# 2 3
# 4 5 6
# 7 8 9 10
rows = int(input("enter: ")
number = 1
for i in range(1, rows+1):
  for j in range(1, i+1):
    print(number, end= " ")
    number += 1
  print()
