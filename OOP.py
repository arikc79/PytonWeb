class Student:

    def __init__(self, name: str, grades: list):
        self.name = name
        self.grades = grades

    def average_grade(self):
        if not self.grades:
            return 0
        return f"студент {self.name} середня оцінка: {sum(self.grades) / len(self.grades):.2f}"


class StudentGroup:

    def __init__(self, students: list = None):
        self.students = students if students else []

    def add_student(self, student: Student):
        self.students.append(student)

    def group_average_grade(self):
        if not self.students:
            return 0

        all_grades = []

        if not self.students:
            return 0

        all_grades = []
        for student in self.students:
            all_grades.extend(student.grades)

        if not all_grades:
            return 0

        total_average = sum(all_grades) / len(all_grades)
        return f"Групова чередня оцінка: {total_average:.2f}"

    def top_student(self):
        if not self.students:
            return "Группа порожня"

        top = max(self.students, key=lambda s: sum(s.grades) / len(s.grades) if s.grades else 0)
        return f"Top студент: {top.name} середня оцінка: {sum(top.grades) / len(top.grades):.2f}"

    def top_student(self):

        if not self.students:
            return "Група порожня"

        # Обчислюємо середню оцінку для кожного студента
        best_student = None
        best_average = -1

        for student in self.students:
            if student.grades:
                avg = sum(student.grades) / len(student.grades)
                if avg > best_average:
                    best_average = avg
                    best_student = student

        if best_student is None:
            return "Немає студентів з оцінками"

        return f"Top студентів: {best_student.name} загал середне значення: {best_average:.2f}"

    def __iter__(self):

        return iter(self.students)

    def __str__(self):

        return f"Розмір групи {len(self.students)} студентів"


student1 = Student("John", [85, 90, 78])
student2 = Student("Alice", [92, 88, 95])
student3 = Student("Bob", [70, 75, 80])

print(student1.average_grade())
print(student2.average_grade())
print(student3.average_grade())

# ===== Тестування StudentGroup =====
print("\n--- Група студентів ---")
group = StudentGroup()
group.add_student(student1)
group.add_student(student2)
group.add_student(student3)

print(group)
print(group.group_average_grade())
print(group.top_student())

print("\nІтерація по студентам групи:")
for student in group:
    print(f"  - {student.name}: {sum(student.grades) / len(student.grades):.2f}")


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
