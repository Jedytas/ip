# Декоратор для проверки корректности входных данных методов thaw и freeze
def validate_args(func):  # Изменение: добавлен декоратор
    """Декоратор для проверки корректности входных данных методов."""
    def wrapper(self, *args, **kwargs):
        if func.__name__ == "thaw":
            steps = args[0]  # Первый аргумент метода thaw — это steps
            if steps < 0 or steps > self.side_length // 2:
                raise ValueError("Некорректное количество шагов для таяния!")
        elif func.__name__ == "freeze":
            n = args[0]  # Первый аргумент метода freeze — это n
            if n < 0:
                raise ValueError("Параметр n для заморозки должен быть неотрицательным!")
        return func(self, *args, **kwargs)
    return wrapper


class SnowFlake:
    def __init__(self, side_length):
        if side_length % 2 == 0:
            raise ValueError("Сторона квадрата должна быть нечетным числом!")
        self.side_length = side_length
        self.snowflake = self._create_snowflake(side_length)

    def _create_snowflake(self, side_length):
        """Создает начальную снежинку в виде квадратной матрицы."""
        matrix = [['-' for _ in range(side_length)] for _ in range(side_length)]
        mid = side_length // 2
        for i in range(side_length):
            for j in range(side_length):
                if i == mid or j == mid or i == j or i + j == side_length - 1:
                    matrix[i][j] = '*'
        return matrix

    @validate_args  # Изменение: декоратор для проверки аргументов thaw
    def thaw(self, steps):
        """Таять снежинку, теряя крайние звездочки с каждой стороны."""
        for _ in range(steps):
            if self.side_length > 1:
                self.side_length -= 2
                self.snowflake = self._create_snowflake(self.side_length)

    @validate_args  # Изменение: декоратор для проверки аргументов freeze
    def freeze(self, n):
        """Замораживать снежинку, увеличивая ее размер на 2 * n и добавляя звездочки."""
        self.side_length += 2 * n
        self.snowflake = self._create_snowflake(self.side_length)

    def thicken(self):
        """Утолщать снежинку, восстанавливая звездочки по параллельным линиям."""
        for i in range(self.side_length):
            for j in range(self.side_length):
                if self.snowflake[i][j] == '*':
                    if i - 1 >= 0:
                        self.snowflake[i - 1][j] = '*'
                    if i + 1 < self.side_length:
                        self.snowflake[i + 1][j] = '*'
                    if j - 1 >= 0:
                        self.snowflake[i][j - 1] = '*'
                    if j + 1 < self.side_length:
                        self.snowflake[i][j + 1] = '*'

    def show(self):
        """Показать снежинку в виде квадратной матрицы."""
        for row in self.snowflake:
            print(' '.join(row))

    def __str__(self):
        """Преобразовать снежинку в строку для вывода."""
        return '\n'.join([' '.join(row) for row in self.snowflake])


class DecoratedSnowFlake(SnowFlake):
    def __init__(self, side_length, decoration):
        super().__init__(side_length)
        self.decoration = decoration

    def decorate(self):
        """Добавить украшение к снежинке."""
        mid = self.side_length // 2
        for i in range(self.side_length):
            for j in range(self.side_length):
                if self.snowflake[i][j] == '*' and (i == mid or j == mid):
                    self.snowflake[i][j] = self.decoration

    def show(self):
        """Показать украшенную снежинку."""
        self.decorate()
        super().show()

    def __str__(self):
        """Преобразовать украшенную снежинку в строку для вывода."""
        self.decorate()
        return super().__str__()


# Пример использования
snowflake = SnowFlake(5)
print("Исходная снежинка:")
snowflake.show()

snowflake.thaw(1)  # Корректное число шагов
print("\nПосле таяния на 1 шаг:")
snowflake.show()

snowflake.freeze(2)  # Корректное значение n
print("\nПосле заморозки:")
snowflake.show()

# Попытка вызвать с некорректными данными:
try:
    snowflake.thaw(10)  # Некорректное число шагов
except ValueError as e:
    print(f"\nОшибка: {e}")