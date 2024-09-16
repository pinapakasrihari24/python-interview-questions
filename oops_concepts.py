class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        return f"{self.name} is a {self.position} earning ${self.salary} annually."

employee1 = Employee("John Doe", "Manager", 75000)
employee2 = Employee("Jane Smith", "Developer", 60000)
print(employee1.display_info())