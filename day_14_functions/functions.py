# def calculate_sum(num1, num2):
#     sum = num1 + num2

# Types of Function Arguments
# 1. Required Argument (Positional Argument)
# 2. Keyword Argument
# 3. Default Argument
# 4. Arbitrary Argument (*args)
# 5. Arbitrary Keyword Argument (**Kwargs) 

# Required Argument


# Keyword Argument

# def greet(name, age):
#     print(f"Hello {name} you are {age} years old")


# greet(age= 23, name= "Indra")


# Write a function that takes two numbers as argument and returns their sum. 
# 1. Call the function using keyword argument and print the returned value.


# def calculate_sum(number_1, number_2):
#     return number_1 + number_2

# returned_value =  calculate_sum(number_1= 1, number_2= 5)
# print(returned_value)

# Write a python program that ask two number and a arthimatic operation 
# (+, -, /, *)
# from user can on the basis of the arithmatic operation provided by the
# user, calculate its value. To calculate and print its value, create function for each operations. Use keyword argument to call the functions.


num1 = int(input("Enter first Number="))
num2 = int(input('Enter second number='))
choice = input("Enter your choice (+ , - , *, /)= ")

def addition(num1, num2):
    print(f"The sum is {num1 + num2}")

def subtraction(num1, num2):
    print(f"The subtraction is {num1 - num2}")

def multiplication(num1, num2):
    print(f"The multiplication is {num1 * num2}")

def division(num1, num2):
    print(f"The division is {num1/num2}")

if choice == '+':
    addition(num1 = num1, num2= num2)
elif choice == '-':
    subtraction(num1 = num1 , num2 = num2)
elif choice == '/':
    division(num1= num1 , num2= num2)
elif choice == '*':
    multiplication(num1 = num1 , num2 = num2)

else:
    print("Invalid Choice.")
