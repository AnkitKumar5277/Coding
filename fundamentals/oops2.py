# single inheritence
class Father: # base class
    def car(self):
        print("Father ki car hai")

class Son(Father):
    def bike(self): # derived class
        print("son ki bike hai")

s = Son()
s.car()
s.bike()

# 👨‍👩‍👦 2. Multiple Inheritance
class Mother:
    def cooking(self):
        print("Mother ko cooking aati hai")

class Father:
    def driving(self):
        print("father ko driving aati hai")

class Child(Mother, Father):
    def study(self):
        print("child padhai karta h")

c = Child()
c.cooking()
c.driving()
c.study()

# 🪜 3. Multilevel Inheritance
class GrandFather:
    def house(self):
        print("grandfather ka house haI")

class Father(GrandFather):
    def car(self):
        print("father ki car hai")

class Son(Father):
    def bike(self):
        print("son ki bike hai")

s = Son()
s.house()
s.car()
s.bike()
print("---------------")

# 🌳 4. Hierarchical Inheritance
class Subject:
    def base(self):
        print("base subject: science")

class Physics(Subject):
    def topic(self):
        print("Topic: Motion")

class Chemistry(Subject):
    def topic(self):
        print("Topic: Atoms")

p = Physics()
c = Chemistry()
p.base()
p.topic()
c.topic()
print("--------------")

# ⚙️ 5. Hybrid Inheritance (Combination)
class A:
    def displayA(self):
        print("class A")
class B(A):
    def displayB(self):
        print("class B")
class C(A):
    def displayC(self):
        print("class C")
class D(B, C):
    def displayD(self):
        print("class D")
d = D()
d.displayA()
d.displayB()
d.displayC()
d.displayD()

# 🧩 6. super() Method
print("--------------")
class Employee:
    def __init__(self, name):
        self.name = name

class Programmer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

p = Programmer("Ankit", "Python")
print(p.name)
print(p.language)

# 🏷️ 7. Class Method
class Student:
    college = "IGNOU"
    @classmethod
    def info(cls):
        print("College name:", cls.college)

Student.info()

# 🏡 8. @property Decorator
class Employee:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
e = Employee("Ankit")
print(e.name)

# 🔐 9. Getters and Setters
class Employee:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

e = Employee("Ankit")
print(e.name)
e.name = "Hadin"
print(e.name)

# ➕ 10. Operator Overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y}"


p1 = Point(2, 3)
p2 = Point(4, 5)
print(p1 + p2)

# 🎀 11. Decorator
def decorator(func):
    def wrapper():
        print("Cake decorate kar rahe h")
        func()
        print("Decoration done")
    return wrapper()

@decorator
def make_cake():
    print("cake ready ho gaya")

# make_cake()

# 📜 12. List Comprehension
squares = []
for i in range(5):
    squares.append(i*i)
print(squares)

squares = [i * i for i in range(5)]
print(squares)

# 📚 13. Dictionary Comprehension
numbers = [1,2,3,4]
squares = {}
for n in numbers:
    squares[n] = n * n
print(squares)

squares = {n: n*n for n in numbers}
print(squares)



