# Create list containing 5 numbers: 5,6,8,4 and 10 and find its total sum using for loop.


# numbers = [5, 6, 8, 4, 10]
# sum = 0

# for number in numbers:
#     sum = sum + number

# print("The total sum is ${sum}")

# Create a dictionary containing marks of 5 subjects: maths = 90, science= 80, english= 70, hindi = 60, social = 50. Find the total sum using for loop.


# subjects = {
#     "maths" : 90,
#     "science": 80,
#     "english": 70,
#     "hindi": 60,
#     "social": 50
# }

# sum = 0
# for value in subjects.values():
#     sum = sum + value

# print(f"The Sum is {sum}")


# Print all even numbers from 1 to 10 using while loop.

# Create a multiplication table of 5 using while loop.
# Output:
# 5x1=5
# 5x2=10
# ...
# 5* 10 = 50


# i = 1
# while i<=10:
#     mul = 5 * i
#     print(f"5x{i}={mul}")
#     i = i + 1



# Find sum of even numbers from 1 to 10 using while loop.

# i = 1
# sum = 0
# while i<=10:
#     if i % 2 == 0:
#         sum = sum + i
#     i = i + 1

# print(f"Sum = {sum}")
    


# i = 1 
# while i<= 10:
#     if(i == 5):
#         break
#     print(i)
#     i = i + 1


# numbers = [4,67,6,5,8,12,65]
# Search 5 from above numbers, if the number found print "Number found" other wise print "Number not found"

# numbers = [4,67,6,5,8,12,65]
# searching_number = int(input("Enter a number to search:"))

# for number in numbers:
#     if number == searching_number:
#         print(f"{searching_number} found")
#         break
# else:
#     print(f"{searching_number} not found")





# Continue to ask for input until the user enters number greater than 20

while True:
    number = int(input("Enter a number="))

    if(number > 20):
        print("You have entered valid number.✔️")
        break;
    else:
        print("Invalid Input.❌")


# Create a CLI TO DO application. User should able to add task, view task, mark the task as completed and remove the task.
        
# To-Do List Manager
# 1. Add Task
# 2. Mark as Completed
# 3. View Tasks
# 4. Remove Task
# 5. Exit
# Enter your choice (1-5):
 