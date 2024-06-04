# Create a class called Rectangle with a constructor that initializes two attributes: length and width. Implement a method within the class called calculate_area() that calculates and returns the area of the rectangle. Lastly, instantiate an object of the Rectangle class with length = 5 and width = 3 and print its area.

# class Rectangle:
#     def __init__(self, x, y):
#         self.length = x
#         self.width = y

#     def calculate_area(self):
#         area = self.length * self.width
#         return area
    
# rectangle = Rectangle(x = 5, y = 3)
# rectangle_area =  rectangle.calculate_area()
# print(f"The total area of rectangle is {rectangle_area}")


# ====================
# Create a class named Counter with a constructor that initializes a single attribute called count with an initial value of 0. Implement two methods within the class. 

# - increment(), which increases the value of count by 1 and prints its value.

# reset(), which sets the value of count to back to 0 
# Additionally create an instance of the Counter class. Call the increment() method three times and then call the reset() method to reset the count.

# class Counter:
#     def __init__(self):
#         self.count = 0

#     def increment(self):
#         self.count = self.count + 1
#         print(f"Counter value is {self.count}")

#     def reset(self):
#         self.count = 0
#         print(f"Counter value resets to {self.count}")

# counter = Counter()
# counter.increment()
# counter.increment()
# counter.increment()
# counter.reset()