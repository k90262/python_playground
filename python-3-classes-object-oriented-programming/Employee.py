class Employee:
    def __init__(self):
        self.name = "Ji-Soo"
        self.__dict__["age"] = 38
        self.__dict__["position"] = "developer"
        self.__dict__["salary"] = 12000

e = Employee()
print(e)
print(e.__class__)
print(e.__dict__)
print(__name__)
print(e.name)
