import random


def quick_sort_deck(deck):
    # Если в колоде менее четырех карт, просто сортируем их
    if len(deck) < 4:
        return sorted(deck)

    # Выбираем опорную карту
    pivot = random.choice(deck)

    left = [card for card in deck if card < pivot]
    right = [card for card in deck if card > pivot]
    middle = [card for card in deck if card == pivot]

    sorted_left = quick_sort_deck(left)
    sorted_right = quick_sort_deck(right)

    # Объединяем отсортированные части
    return sorted_left + middle + sorted_right


# Пример использования
deck = [4, 2, 7, 1, 3, 5]
sorted_deck = quick_sort_deck(deck)
print(sorted_deck)  # Ожидаемый вывод: [1, 2, 3, 4, 5, 7]

# Тест 1
assert quick_sort_deck([4, 2, 7, 1, 3, 5]) == [1, 2, 3, 4, 5, 7]
# Тест 2
assert quick_sort_deck([10, 5, 3, 8]) == [3, 5, 8, 10]
# Тест 3
assert quick_sort_deck([1]) == [1]
# Тест 4
assert quick_sort_deck([3, 2]) == [2, 3]
# Тест 5
assert quick_sort_deck([7, 3, 3, 4, 1, 2, 5]) == [1, 2, 3, 3, 4, 5, 7]
print("OK!")