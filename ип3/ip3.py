# На олимпиаде участвовало N человек, каждый из которых мог набрать от 0 до 100 баллов.
# Жюри может наградить не более 45% участников, округляя число призеров вниз.
# Если последний из призеров набрал столько же баллов, сколько первый из не-призеров, то они и все с таким же результатом становятся призерами. 
# Программа должна определить минимальный балл участника, который стал призером.

# Программа получает на вход файл с информацией об участниках олимпиады (один участник - в одной строке). 
# Строка содержит имя участника (текстовая строка с произвольным числом пробелов) и набранный данным участником балл через пробел.

# Решение должно использовать O(1) памяти, то есть нельзя использовать списки, длина которых зависит от длины входных данных

import math

def get_min_prize_score(file_path):
    all_participants = 0
    scores_count = [0] * 101  # Счетчики для каждого балла от 0 до 100

    # Подсчет количества участников и частот баллов
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            all_participants += 1
            _, score = line.rsplit(' ', 1)  # Разделяем имя и балл
            score = int(score.strip())
            scores_count[score] += 1

    # Определяем количество призеров
    max_winners = math.floor(all_participants * 0.45)

    # Найти минимальный балл призера
    current_winners = 0
    for score in range(100, -1, -1):  # Идем от максимального к минимальному баллу
        current_winners += scores_count[score]
        if current_winners >= max_winners:
            return score

    return 0  # Если призеров нет (маловероятно для N > 0)

# Пример использования
file_path = r'C:\Users\HomeStationPC\Desktop\ип\participants.txt'  # Путь к вашему файлу
min_prize_score = get_min_prize_score(file_path)
print(f"Минимальный балл призера: {min_prize_score}")
