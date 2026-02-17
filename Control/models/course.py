class Course:
    _id_counter = 1

    def __init__(self, title: str, teacher: str):
        self.id = Course._id_counter
        Course._id_counter += 1

        self.title = title
        self.teacher = teacher

        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def __str__(self):
        student_names = [student.name for student in self.students]

        return (f"Курс\n"
                f"  ID: {self.id}\n"
                f"  Назва: {self.title}\n"
                f"  Викладач: {self.teacher.name}\n"
                f"  Кількість студентів: {len(self.students)}\n"
                f"  Студенти: {student_names if student_names else 'немає'}")
