# main.py

from models.student import Student
from models.teacher import Teacher
from models.services.enrollment_service import EnrollmentService
from models.services.exceptions import CourseManagementError


def main():
    try:
        # 1️⃣ Створюємо викладача
        teacher = Teacher("Іван Петренко")

        # 2️⃣ Створюємо студентів
        student1 = Student("Олег Коваль")
        student2 = Student("Марія Шевченко")

        # 3️⃣ Викладач створює курс
        python_course = EnrollmentService.create_course("Python для початківців", teacher)

        # 4️⃣ Запис студентів
        EnrollmentService.enroll_student(student1, python_course)
        EnrollmentService.enroll_student(student2, python_course)

        # 5️⃣ Виставлення оцінок
        EnrollmentService.assign_grade(student1, python_course, 95)
        EnrollmentService.assign_grade(student2, python_course, 88)

        # 6️⃣ Вивід стану системи
        print(teacher)
        print()
        print(python_course)
        print()
        print(student1)
        print()
        print(student2)

        # 7️⃣ Перевірка заборони (студент створює курс)
        print("\n--- Перевірка заборони ---")
        EnrollmentService.create_course("Нелегальний курс", student1)

    except CourseManagementError as e:
        print(f"\n[ПОМИЛКА СИСТЕМИ]: {e}")

    except Exception as e:
        print(f"\n[НЕОЧІКУВАНА ПОМИЛКА]: {e}")


if __name__ == "__main__":
    main()
