class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)

    def __str__(self):
        return f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of {self.salary}"

    def __repr__(self):
        return (
            f"Employee("
            f"name={repr(self.name)}, "
            f"age={repr(self.age)}, "
            f"position={repr(self.position)}, "
            f"salary={repr(self.salary)})"
        )

    def __add__(self, other):
        return Employee("New", self.age + other.age, "dev", 2000)

employee1 = Employee("Ji-Soo", 38, "developer", 1200)
employee2 = Employee("Lauren", 44, "tester", 1000)
print(employee1)
print(employee1.__class__)
print(employee1.__dict__)
print(__name__)
print(employee1.name)

print(eval(repr(employee1)))

employee3 = employee1.__add__(employee2)
employee4 = employee1+employee2
print(employee4)
assert(str(employee3) == str(employee4))

