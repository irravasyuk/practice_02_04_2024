# Завдання 1
class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Ділити на 0 не можна"

    def __call__(self, a, b, operation):
        if operation == 'add':
            return self.add(a, b)
        elif operation == 'sub':
            return self.sub(a, b)
        elif operation == 'mul':
            return self.mul(a, b)
        elif operation == 'div':
            return self.div(a, b)
        else:
            print('Такої операції немає')

calculator = Calculator()
print('Додавання:', calculator(2, 3, 'add'))
print('Віднімання:', calculator(5, 2, 'sub'))
print('Множення:', calculator(2, 3, 'mul'))
print('Ділення:', calculator(6, 2, 'div'))




# Завдання 2
# Створіть дескриптор для атрибуту, що зберігає
# розмір файлу. Додайте можливість зберігати розмір
# файлу в байтах, але представляти його у зручному для
# читання форматі (наприклад, КБ або МБ).
class FileSize:
    def __init__(self, unit=None):
        self.unit = unit

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.convert_to_unit(instance.size)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Файл має неправильний розмір')
        instance.size = value

    def convert_to_unit(self, size):
        if self.unit:
            mult = {'KB': 1024, 'MB': 1024 * 1024}.get(self.unit)
            if mult is None:
                raise ValueError('Використовуйте KB або MB')
            size /= mult
            if size < 1024:
                return f"{size:.2f} KB"
            else:
                return f"{size / 1024:.2f} MB"
        return f"{size} B"


class MyClass:
    file_size = FileSize()

    def __init__(self, size_in_bytes):
        self.size = size_in_bytes


my_instance = MyClass(12345678)
print(my_instance.file_size)



# Завдання 4
class User:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if 0 <= value <= 120:
            self._age = value
        else:
            raise ValueError('Вік має бути в межах від 0 до 120')

user = User('Ivan', 29)
print(user.age)

#user.age = 121