import random

for _ in range(77):  # 30 циклов
  
    print("click 61 956")
    print("delay 5000")

    #1 клик

    t = random.randint(3000, 5000)
    x = random.randint(42, 411)
    y = random.randint(343, 725)
    print(f"click {x} {y}")
    print(f"delay {t}")

    x2 = random.randint(150, 399)
    y2 = random.randint(910, 937)
    print(f"click {x2} {y2}")
    print("delay 1500")

    #2 клик

    t = random.randint(3000, 5000)
    x = random.randint(42, 411)
    y = random.randint(343, 725)
    print(f"click {x} {y}")
    print(f"delay {t}")

    x2 = random.randint(150, 399)
    y2 = random.randint(910, 937)
    print(f"click {x2} {y2}")
    print("delay 1500")

    #3 клик

    t = random.randint(3000, 5000)
    x = random.randint(42, 411)
    y = random.randint(343, 725)
    print(f"click {x} {y}")
    print(f"delay {t}")

    x2 = random.randint(150, 399)
    y2 = random.randint(910, 937)
    print(f"click {x2} {y2}")
    print("delay 1500")

    #4 клик

    t = random.randint(3000, 5000)
    x = random.randint(42, 411)
    y = random.randint(343, 725)
    print(f"click {x} {y}")
    print(f"delay {t}")

    x2 = random.randint(150, 399)
    y2 = random.randint(910, 937)
    print(f"click {x2} {y2}")
    print("delay 1500")

    #5 клик

    t = random.randint(3000, 5000)
    x = random.randint(42, 411)
    y = random.randint(343, 725)
    print(f"click {x} {y}")
    print(f"delay {t}")

    x2 = random.randint(150, 399)
    y2 = random.randint(910, 937)
    print(f"click {x2} {y2}")
    print("delay 1500")

    #6 клик

    t = random.randint(3000, 5000)
    x = random.randint(42, 411)
    y = random.randint(343, 725)
    print(f"click {x} {y}")
    print(f"delay {t}")

    x2 = random.randint(150, 399)
    y2 = random.randint(910, 937)
    print(f"click {x2} {y2}")
    print("delay 1500")

    #7 клик

    t = random.randint(3000, 5000)
    x = random.randint(42, 411)
    y = random.randint(343, 725)
    print(f"click {x} {y}")
    print(f"delay {t}")

    x2 = random.randint(150, 399)
    y2 = random.randint(910, 937)
    print(f"click {x2} {y2}")
    print("delay 1500")

    #8 клик

    t = random.randint(3000, 5000)
    x = random.randint(42, 411)
    y = random.randint(343, 725)
    print(f"click {x} {y}")
    print(f"delay {t}")

    x2 = random.randint(150, 399)
    y2 = random.randint(910, 937)
    print(f"click {x2} {y2}")
    print("delay 1500")

    #Клик на колво монет

    x = random.randint(236, 315)
    y = random.randint(120, 146)
    print(f"click {x} {y}")
    print("delay 3232")

    #Клик на сбор монет

    x = random.randint(116, 436)
    y = random.randint(553, 577)
    print(f"click {x} {y}")
    print("delay 2323")

    #Выход из меню сбора монет

    print("click 33 71")
    print("delay 750")
    print("click 33 71")
    print("delay 4800000")

    print()
    print()
input("Нажмите Enter для выхода...")




import random
import sys

# Открываем файл для записи с расширением .txt
with open('output.txt', 'w') as f:
    # Перенаправляем стандартный вывод в файл
    sys.stdout = f

    for _ in range(77):  # 77 циклов
        print("click 61 956")
        print("delay 5000")

        # 1 клик
        t = random.randint(3000, 5000)
        x = random.randint(42, 411)
        y = random.randint(343, 725)
        print(f"click {x} {y}")
        print(f"delay {t}")

        x2 = random.randint(150, 399)
        y2 = random.randint(910, 937)
        print(f"click {x2} {y2}")
        print("delay 1500")

        # Остальные клики, задержки и действия
        for _ in range(7):  # ещё 7 кликов (итого 8)
            t = random.randint(3000, 5000)
            x = random.randint(42, 411)
            y = random.randint(343, 725)
            print(f"click {x} {y}")
            print(f"delay {t}")

            x2 = random.randint(150, 399)
            y2 = random.randint(910, 937)
            print(f"click {x2} {y2}")
            print("delay 1500")

        # Клик на количество монет
        x = random.randint(236, 315)
        y = random.randint(120, 146)
        print(f"click {x} {y}")
        print("delay 3232")

        # Клик на сбор монет
        x = random.randint(116, 436)
        y = random.randint(553, 577)
        print(f"click {x} {y}")
        print("delay 2323")

        # Выход из меню сбора монет
        print("click 33 71")
        print("delay 750")
        print("click 33 71")
        print("delay 4800000")

        print()  # Пустая строка между циклами
        print()

# Выводим сообщение в консоль, так как sys.stdout возвращён в стандартный вывод
sys.stdout = sys.__stdout__
print("Результаты сохранены в файл 'output.txt'")
input("Нажмите Enter для выхода...")

