# Create a python class called Circle with a constructor that initializes the value of radius of circle. Implement the method within the class called calculate_area() that calculates and returns the area of the circle. Lastly, instantiate an object of the Circle class with radius 5 and print out the area.

# class Circle:
#     def __init__(self, r) -> None:
#         self.radius = r

#     def calculate_area(self):
#         area = 3.1416 * self.radius * self.radius
#         return area

# c1 = Circle(5)



# print("The area of circle is", c1.calculate_area())




class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, value):
        self.__balance = self.__balance + value
        print(f"Your amount {value} deposited successfully")

    def withdraw(self, withdraw_amount):
        if(withdraw_amount < self.__balance):
            print("Insufficient balance")
        else:
            self.__balance = self.__balance - withdraw_amount
            print(f"Your amount {withdraw_amount} withdrawn successfully")

    def view_balance(self):
        return self.__balance

rajat_account = BankAccount()

rajat_account.deposit(500)
print(f"\nAfter deposit the balance is {rajat_account.view_balance()}")

