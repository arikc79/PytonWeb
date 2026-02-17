class CourseManagementError(Exception):
    """
    Базовий виняток системи.
    """
    pass


class PermissionDenied(CourseManagementError):
    """
    Недостатньо прав для виконання операції.
    """
    pass


class AlreadyEnrolled(CourseManagementError):
    """
    Студент вже записаний на курс.
    """
    pass


class NotEnrolled(CourseManagementError):
    """
    Студент не записаний на курс.
    """
    pass


class InvalidGrade(CourseManagementError):
    """
    Некоректне значення оцінки.
    """
    pass
