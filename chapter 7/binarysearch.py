def binary_search(arr, target):
    def search(arr, target, left, right):
        if left > right:
            return -1

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return search(arr, target, left, mid - 1)
        else:
            return search(arr, target, mid + 1, right)

    return search(arr, target, 0, len(arr) - 1)


# Пример использования
sorted_numbers = [1, 2, 3, 4, 5, 6, 7]
index_of_four = binary_search(sorted_numbers, 4)
print(index_of_four)  # Ожидаемый вывод: 3

index_of_eight = binary_search(sorted_numbers, 8)
print(index_of_eight)  # Ожидаемый вывод: -1

# Тест 1
assert binary_search([1, 2, 3, 4, 5, 6, 7], 4) == 3
# Тест 2
assert binary_search([1, 2, 3, 4, 5, 6, 7], 6) == 5
# Тест 3
assert binary_search([1, 2, 3, 4, 5, 6, 7], 1) == 0
# Тест 4
assert binary_search([1, 2, 3, 4, 5, 6, 7], 8) == -1
# Тест 5
assert binary_search([], 1) == -1  # Пустой массив
print("Все тесты пройдены!")