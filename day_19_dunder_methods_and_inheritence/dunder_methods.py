# class Employee:
#     def __init__(self, id, name, salary) -> None:
#         self.id = id
#         self.name = name
#         self.salary = salary

#     def __str__(self) -> str:
#         return f"id = {self.id}, name = {self.name}, salary = {self.salary}"
    
#     def __eq__(self, value) -> bool:
#         return self.salary == value.salary
    
#     def __le__(self, value):
#         return  self.salary <= value.salary


# e1 = Employee(1, "Indra", 30000)
# e2 = Employee(2, "Adarsh", 20000)

# # print(e1 == e2)
# # print(e1.__eq__(e2))

# print(e1 <= e2)



# Inheritance


class Employee:
    def __init__(self, id, name, salary) -> None:
        self.id = id
        self.name = name
        self.salary = salary

    def display_detail(self):
        print(f"Id = {self.id}, Name = {self.name}, salary = {self.salary}")

class Developer(Employee):
    def __init__(self, id, name, salary, language) -> None:
        super().__init__(id, name, salary)
        self.language = language

    def display_detail(self):
        super().display_detail()
        print(f"Language = {self.language}")

d1 = Developer(1, "Indra", 20000, "python")
d1.display_detail()