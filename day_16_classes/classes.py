class Student:
    # name = "Indra"
    # age = 20
    # address = "Kathmandu"

    def __init__(self, name, age, address):
        self.name = name
        self.age= age
        self.address = address
        
    def details(self):
        print(f"name = {self.name}, age = {self.age}, address= {self.address} ")

student1 = Student("Indra", 20,"kathmandu")
student2 = Student("Bishal", 21, "Lalitpur")
student1.details()
student2.details()







# Create a class called Car and create three member variables named model, color and fuel_type and assign its values. Also create a member function called start that prints the values of member variable. Create an object of the car and call the start function. 


# Create a class called Calculator with the following methods.
# 1. add
# 2. subtract
# 3. multiply
# 4. divide

# Pass two values using constructor and print its values using above methods

class Calculator:
    def __init__(self, x, y) -> None:
        self.num1 = x
        self.num2 = y

    def add(self):
        print("The total sum is ", self.num1 + self.num2)

    def subtract(self):
        print("The subtraction is", self.num1 - self.num2)

    def multiply(self):
        pass
    def divide(self):
        pass

calculator = Calculator(5, 2)
calculator.add()
calculator.subtract()





