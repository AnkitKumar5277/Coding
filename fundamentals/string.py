l = [str(i*7) for i in range(1,11)]
print(l)
verticalTable = "\n".join(l)
print(verticalTable)
print("\n".join(l)) # direct method

n = input("Enter your name : ")
m = input("Enter your marks : ")
p = input("Enter your phone number : ")

# Create a list
my_list = ["apple", "banana", "orange", "grape"]
# Accessing elements using index
print("First element:", my_list[0])  # Output: apple
print("Last element:", my_list[-1])   # Output: grape (negative index for last element)
# Accessing a range of elements (slicing)
print("First two elements:", my_list[0:2])  # Output: ['apple', 'banana']

# Create an empty list
my_list = []
# Add elements to the list using append()
my_list.append("Apple")
print(my_list)
