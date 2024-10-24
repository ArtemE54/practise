distance_in_kilometers = float(input("Введите расстояние в километрах: "))
distance_in_meters = float(input("Введите расстояние в метрах: "))
distance_in_kilometers_meters = distance_in_kilometers * 1000
if distance_in_kilometers_meters < distance_in_meters:
    print(f"Наименьшее расстояние: {distance_in_kilometers_meters} метров")
else:
    print(f"Наименьшее расстояние: {distance_in_meters} метров")
