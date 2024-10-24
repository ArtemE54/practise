numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
multiplier = int(input("Введите число для таблицы умножения: "))
print(f"Таблица умножения для числа {multiplier}:")
for number in numbers:
    result = multiplier * number
    print(f"{multiplier} * {number} = {result}")
