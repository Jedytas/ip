# Класс «Снежинка» (SnowFlake)

# При инициализации класс принимает целое нечетное число – сторону квадрата, в который вписана снежинка.

# Методы:
# – thaw() – таять, при этом на каждом шаге пропадают крайние звездочки со всех сторон; параметр показывает, сколько шагов прошло.
# – freeze(n) – намораживаться, при этом сторона квадрата, в который вписана снежинка, увеличивается на 2 * n, одновременно добавляются звездочки в нужных местах, чтобы правило соблюдалось.
# – thicken() – утолщаться, ко всем линиям звездочек с двух сторон добавляются параллельные (если перед этим снежинка таяла, то теперь звездочки восстанавливаются).
# – show() – показывать (рисуется снежинка в виде квадратной матрицы со звездочками и дефисами в пустых местах).

# Создать класс-наследник от класса «Снежинка», например, «Украшенная снежинка». 

# Обязательно использование конструктора, декораторов и метода __str__.


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

    def thaw(self, steps):
        """Таять снежинку, теряя крайние звездочки с каждой стороны."""
        for _ in range(steps):
            if self.side_length > 1:
                self.side_length -= 2
                self.snowflake = self._create_snowflake(self.side_length)

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


# Класс-наследник от SnowFlake
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
snowflake = SnowFlake(9)
print("Исходная снежинка:")
snowflake.show()

snowflake.thaw(1)
print("\nПосле таяния на 1 шаг:")
snowflake.show()

snowflake.thaw(1)
print("\nПосле таяния еще на 1 шаг:")
snowflake.show()

snowflake.freeze(3)
print("\nПосле замораживания на 3 шага:")
snowflake.show()

snowflake.thicken()
print("\nПосле утолщения снежинки:")
snowflake.show()

decorated_snowflake = DecoratedSnowFlake(9, '#')
print("\nУкрашенная снежинка:")
print(decorated_snowflake)
