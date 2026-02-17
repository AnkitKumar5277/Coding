# Python Program to Find the Sum of Natural Numbers
num = 16
if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)
# The sum is 136

# Write a function to find the sum of first N natural numbers.
# Hint: The formula for the sum of the first N natural numbers is N*(N+1)/2.
# For example, for input 5, the outout should be 15.
def sum_of_natural_numbers(n):
    if n < 1:
        return "Input must be a positive integer."
    return n * (n + 1) // 2  # Using integer division for an exact result
number = 5
result = sum_of_natural_numbers(number)
print(f"The sum of the first {number} natural numbers is {result}.")

