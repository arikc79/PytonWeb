# 1
# def reverse_string(s: str) -> str:
#     if len(s) <= 1:
#         return s
#
#     return reverse_string(s[1:]) + s[0]
#
#
# # 2
# def revers(s, i=0):
#     if len(s) <= 1:
#         return s
#
#     if i >= len(s):
#         return ""
#     return revers(s, i + 1) + s[i]
#
#
# if __name__ == "__main__":
#     print(revers("ТІВИРП, World!"))


# class Car:
#     def __init__(self, make: str, model: str, year: int):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def __str__(self):
#         return f"{self.year} {self.make} {self.model}"
#
#
# car = Car("Mercedes", 'E-Class', 2020)
#
# print(car)
#
# car.year = 2021
# car.model = "5 Series"
# car.make = "BMW"
#
# print(car)

#
# class Student:
#     def __init__(self, name: str, grade: int):
#         self.name = name
#         self.grade = grade
#
#     def is_passed(self):
#         return True if self.grade >= 60 else False
#
#     def __str__(self):
#         return f"{self.name},  grade:{self.grade}"
#
#
# s1 = Student("John", 75)
# s2 = Student("Alice", 55)
#
# print(s1)
# print(s2)
#
# print(s1.is_passed())
# print(s2.is_passed())

#
# class Rectangle:
#     def __init__(self, width: int, heigth: int):
#         self.width = width
#         self.heigth = heigth
#
#     def area(self):
#         return self.width * self.heigth
#
#     def perimeter(self):
#         return 2 * (self.width + self.heigth)
#
#     def __str__(self):
#         return f"Прямокутник: ширина={self.width}, висота={self.heigth}"
#
#
# r = Rectangle(6, 5)
# print(r)
# print(f"площа = {r.area()}")
# print(f"периметр = {r.perimeter()}")


# class Counter:
#     def __init__(self, value):
#         self.value = value
#
#     def increment(self):
#         self.value += 1
#
#     def decrement(self):
#         self.value -= 1
#
#     def __str__(self):
#         return f"Лічильник значення: {self.value}"
#
# c = Counter(2)
#
# c.decrement()
#
# c.increment()
# c.increment()
# c.increment()
#
# print(c)

class BankAccont:
    def __init__(self, owner: str, balance: float = 0.):
        self.owner = owner
        self.balance = balance

    def depost(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"Депозит успішний. Новий баланс: {self.balance}")
        else:
            print("Сума депозиту повинна бути додатною.")

    def withdraw(self, amount: float):
        if amount > self.balance:
            print("Недостатньо коштів для зняття.")
        elif amount <= 0:
            print("Сума зняття повинна бути додатною.")
        else:
            self.balance -= amount
            print(f"Зняття успішне. Новий баланс: {self.balance}")

    def __str__(self):
        return f"Банківський рахунок власника: {self.owner}, баланс: {self.balance}"


acc = BankAccont("Alice", 100_000)
acc.depost(5000)
acc.withdraw(20_000)
acc.withdraw(200_000)
print(acc)


class Car:
    def __init__(self, model, color, year, make):
        self.model = model
        self.color = color
        self.year = year
        self.make = make

    def __repr__(self):
        return (f"Car(model={self.model!r}, "
                f"color={self.color!r}, "
                f"year={self.year}, "
                f"make={self.make!r})")

    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.color})"


car1 = Car("Model S", "Red", 2020, "Tesla")
print(car1)

print(repr(car1))
