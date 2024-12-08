def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Разделяем массив на две половины
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Рекурсивно сортируем каждую половину
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Объединяем отсортированные половины
    return merge(left_half, right_half)


def merge(left, right):
    sorted_arr = []
    left_index, right_index = 0, 0

    # Сравниваем элементы из двух отсортированных массивов и добавляем меньший элемент в новый массив
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_arr.append(left[left_index])
            left_index += 1
        else:
            sorted_arr.append(right[right_index])
            right_index += 1

    # Добавляем оставшиеся элементы из левой половины
    sorted_arr.extend(left[left_index:])

    # Добавляем оставшиеся элементы из правой половины
    sorted_arr.extend(right[right_index:])

    return sorted_arr


# Пример использования
numbers = [38, 27, 43, 3, 9, 82, 10]
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)  # Ожидаемый вывод: [3, 9, 10, 27, 38, 43, 82]

# Тест 1
assert merge_sort([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]
# Тест 2
assert merge_sort([10, 7, 8, 9]) == [7, 8, 9, 10]
# Тест 3
assert merge_sort([1]) == [1]
# Тест 4
assert merge_sort([3, 3, 3, 2, 2]) == [2, 2, 3, 3, 3]
# Тест 5
assert merge_sort([]) == []
print("OK!")