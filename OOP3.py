class TemperatureSensor:

    def __init__(self, temperature):

        self.__temperature = None
        self.set_temperature(temperature)

    def get_temperature(self):
        return self.__temperature

    def get_temperature_fahrenheit(self):
        return self.__temperature * 9 / 5 + 32

    def set_temperature(self, temperature):
        if not isinstance(temperature, (int, float)):
            raise TypeError("Температура повинна бути числом")
        if temperature > 100 or temperature < -100:
            raise ValueError("Температура повинна бути в діапазоні від -100 до 100 градусів Цельсія")
        self.__temperature = temperature

    def __repr__(self):
        return f"TemperatureSensor({self.__temperature}°C)"


if __name__ == "__main__":
    s = TemperatureSensor(25)
    print("Температура (°C):", s.get_temperature())
    print("Температура (°F):", s.get_temperature_fahrenheit())

    s.set_temperature(-100)
    print("Після set -100:", s)

    try:
        s.set_temperature(200)
    except Exception as e:
        print("Помилка при set_temperature(200):", type(e).__name__, e)


# 2

class PasswordManager:
    def __init__(self, password):
        self.__password = None
        self.set_password(password)

    def set_password(self, password):
        if not isinstance(password, str):
            raise TypeError("Пароль має бути рядком")
        if len(password) < 6:
            raise ValueError("Пароль має бути не меньше 6 символів")
        self.__password = password

    def check_password(self, password):
        return self.__password == password

    def change_password(self, old_password, new_password):
        if not self.check_password(old_password):
            raise ValueError("Старий пароль не правильний")
        if len(new_password) < 6:
            raise ValueError("Пароль має бути не меньше 6 символів")
        self.__password = new_password


# 3

class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def check_password(self, password):
        return self.__password == password

    def get_username(self):
        return self.__username

    def change_password(self, old_password, new_password):
        if not self.check_password(old_password):
            raise ValueError("Старий пароль не правильний")
        if len(new_password) < 6:
            raise ValueError("Пароль має бути не меньше 6 символів")


class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.__permissions = set()

    def reset_password(self, user, new_password):
        if not isinstance(user, User):
            raise TypeError("Можна скинути пароль тільки для об'єкта User")
        user.change_password(user._User__password, new_password)


user1 = User("user1", "password123")

admin1 = Admin("admin1", "")

print(user1.get_username())
admin1.reset_password(user1, "newpassword456")
print(user1.check_password("newpassword456"))  # True
