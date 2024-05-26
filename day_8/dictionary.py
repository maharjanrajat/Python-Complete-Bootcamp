# Create a phonebook using python dictionary named 'phonebook' with at least
# 5 key-value pairs. Each key should represent person's name and each value should 
# represent phone numbers.

# 1. print the phonebook
# 2. Add new item to the phonebook
# 3. update phone number of one of the person
# 4. print the phonbook
# 5. print the values of phonebook using for loop


# if customer by a product and if total price is greater than 1000, then give 10% discount otherwise give 5% discount. Print the discount value and total amount to be paid.

# Write a Python Program to get a number from user and check if a given number is odd or even. If the number is even, print "The number is even" otherwise print "The number is odd". 

# Create a Python program that takes two integers as input and determines the larger one. If they are equal, print "Both are equal" otherwise print one is greater than other.
 

# num_1 = int(input("Enter first number:"))
# num_2 = int(input('Enter second number:'))


# Create a Python program that checks if a given number is divisible by 3 and 5. If it is divisible by both, print " The number is divisible by both 3 and 5" otherwise print "The number is not divisible by both 3 and 5".


# number = int(input('Enter a number:'))

# if number %3 == 0 and number %5 == 0:
#     print(f"{number} is divisible by 3 and 5")
# else:
#     print(f"{number} is not divisible by both 3 and 5")


value = "4"

match value:
    case int(value):
        print("The number is integer")
    case float(value):
        print('The number is float')
    case str(value):
        print('The number is string')
    case _:
        print("Unknown value")


# Write a python program that takes any number between 1 to 7 and print the week day of that number using match statement.