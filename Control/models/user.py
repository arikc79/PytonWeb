class User:
    _id_counter = 1

    def __init__(self, name: str):
        self.id = User._id_counter
        User._id_counter += 1

        self.name = name

    def __str__(self):
        # Виправлено: видалено зайву дужку у кінці рядка
        return f"{self.__class__.__name__}(id={self.id}, name={self.name})"
