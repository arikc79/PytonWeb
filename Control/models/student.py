from models.user import User
from models.services.exceptions import InvalidGrade


class Student(User):

    def __init__(self, name: str):
        super().__init__(name)

        self.courses = []
        self.grades = {}

    # Додаємо курс до студента
    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    # Встановлюемо оцінку для курсу
    def set_grades(self, course_id: int, grade: int):
        if not (0 <= grade <= 100):
            raise InvalidGrade("Оцінка має бути від 0 до 100")

        self.grades[course_id] = grade

    def __str__(self):
        # Формуємо список назв курсів
        course_titles = [course.title for course in self.courses]

        # Формуємо список оцінок
        grades_info = [f"курс_id={course_id}: {grade}" for course_id, grade in self.grades.items()]

        return (f"Студент\n"
                f"  ID: {self.id}\n"
                f"  Ім'я: {self.name}\n"
                f"  Курсів: {len(self.courses)}\n"
                f"  Список курсів: {course_titles if course_titles else 'немає'}\n"
                f"  Оцінки: {grades_info if grades_info else 'немає'}")
