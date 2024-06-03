# Default Arguemnts

# - it is used to provide default value to a paramter


# def greet(age, name = "User"):
#     print(f"Hello {name} you are {age} years old")

# greet( name = "Rajat", age = 23)



# Create a function called total price that takes price as positional arguement and discount percent as default argument. If discount percent is not passed when calling the function, use 5% as the default discount percentage. Print the final value after the discount

# def total_price(price, discount_percent = 5):

#     discount = price * discount_percent /100
#     discounted_price = price - discount
#     print(f"The price after discount is {discounted_price}")

# total_price(4000)


# def average(a, b):
#     average = (a+b)/2
#     print(f"The average is  {average}")

# average(4,5)



# Arbitrary Argument
# - Also known as variable length arguments
# - Allows us to pass any number of arguments to the function
#- The parameter name is prefixed with *
# The arguements are stored in a tuple
# If we don't know how many arguments to pass to a function, then we can use this type of arguements
# Generally, denoted as *args

# def names(*args):
#     for name in args:
#         print(name)

# names("Rajat", "indra", "prayush")


# def total_multiplied_value(*numbers):
#     total_value = 1
#     for number in numbers:
#         total_value = total_value * number
#     return total_value

# print(total_multiplied_value(2,3,5,6,67,7))

# Create a arbitrary function that takes any number of integer values and find its average.


# def numbers_average(*numbers):
#     total_sum = 0
#     for number in numbers:
#         total_sum = total_sum + number

#     average = total_sum/len(numbers)
#     print(f"The average is {average}")

# numbers_average(23,4,65,76,2)


# Create a function that takes arbitary argument as parameter and find its sum.

# def total_sum(*numbers):
#     sum = 0 
#     for number in numbers:
#         sum = sum + number
#     return sum

# def average(sum, total_number):
#     average_value = sum/total_number
#     print(f"Total average = {average_value}")


# total_sum_value = total_sum(3,4,5,6,7)

# average(total_sum_value, 5)




# def greeting(**kwargs):
#     print(type(kwargs))

# greeting(age=  20, name = "Rajat")


# Create a python function called print_info that takes person's name, age, profession and address as arbitrary keyword argument and print their information in the following format.

# Name: <value>
# Age: <value>
# Profession: <value>
# {
#     "name": "Ranjit",
#     "age": 22,
#     'professon': "software dev"
# }


name = input('Enter person name=')
age = int(input("Enter person age="))
profession = input("Enter person profession=")

def print_info(**infos):
    for key, value in infos.items():
        print(f"{key}: {value}")

print_info(
    name = name,
    age = age,
    profession = profession
    )