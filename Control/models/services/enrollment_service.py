from models.course import Course
from models.student import Student
from models.teacher import Teacher
# Виправлено: імпорт exceptions з правильного шляху models.services
from models.services.exceptions import (PermissionDenied, AlreadyEnrolled, NotEnrolled, )


class EnrollmentService:

    @staticmethod
    def create_course(title: str, teacher):
        """
        Створення курсу.
        Доступно тільки викладачу.
        """
        if not isinstance(teacher, Teacher):
            raise PermissionDenied("Тільки вчителі можуть створювати курси")

        course = Course(title, teacher)

        # двосторонній зв'язок
        teacher.add_course(course)

        return course

    @staticmethod
    def enroll_student(student, course):
        """
        Запис студента на курс.
        """
        if not isinstance(student, Student):
            raise PermissionDenied("Тільки студенти можуть записатися на курси")

        if student in course.students:
            raise AlreadyEnrolled("Студент вже зарахований на цей курс")

        # синхронізація
        course.add_student(student)
        student.add_course(course)

    @staticmethod
    def assign_grade(student, course, grade: int):
        """
        Виставлення оцінки.
        """
        if student not in course.students:
            raise NotEnrolled("Студент не зарахований на цей курс")

        # Виправлено: змінено set_grade на set_grades (правильна назва методу)
        student.set_grades(course.id, grade)

    @staticmethod
    def get_student_courses(student):
        """
        Повертає список курсів студента.
        """
        if not isinstance(student, Student):
            raise PermissionDenied("Тільки студенти мають курси")

        return student.courses

    @staticmethod
    def get_course_students(course):
        """
        Повертає список студентів курсу.
        """
        return course.students
