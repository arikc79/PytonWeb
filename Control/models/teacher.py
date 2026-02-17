from models.user import User


class Teacher(User):
    def __init__(self, name: str):
        super().__init__(name)
        self.courses = []

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def __str__(self):
        course_titles = [course.title for course in self.courses]

        return (f"Викладач\n"
                f"  ID: {self.id}\n"
                f"  Ім'я: {self.name}\n"
                f"  Кількість курсів: {len(self.courses)}\n"
                f"  Курси: {course_titles if course_titles else 'немає'}")
