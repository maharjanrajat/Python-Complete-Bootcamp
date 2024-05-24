# countries = [
#     "Nepal",
#     "India",
#     "China",
#     "Japan",
#     "Russia"
# ]

# for country in countries:
#     print(country)


# Create a list named "fruits" and assign 3 fruits to it.
# 1. Print the value of fruits variable
# 2. Add 2 more fruits at the last of the fruits list
# 3. Print the value of the variable.
# 4. remove 1 fruit from the list.
# 5. Print the value of the variable

# Slice first 3 values and print
# Slice last 3 values and print
# Reverse the list

# fruits = ['apple', 'banana', 'grapes']

# print(fruits[::-1])

import sys

fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = ('apple', 'banana', 'orange')


print("List Memory", sys.getsizeof(fruits_list))
print("Tuple Memory", sys.getsizeof(fruits_tuple))