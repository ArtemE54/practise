a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
if b % a == 0:
    print(f"{a} является делителем {b}")
else:
    print(f"{a} не является делителем {b}")
