def is_perfect_square(n):
    if n < 0:
        return False
    root = int(n ** 0.5)
    return root * root == n


def generate_permutations(s):
    if len(s) == 1:
        return {s}

    permutations = set()
    for i in range(len(s)):
        for perm in generate_permutations(s[:i] + s[i + 1:]):
            permutations.add(s[i] + perm)

    return permutations


def count_perfect_squares(num):
    str_num = str(num)
    unique_permutations = generate_permutations(str_num)
    count = sum(1 for perm in unique_permutations if is_perfect_square(int(perm)))

    return count


def sort_by_perfsq(arr):
    counts = [(count_perfect_squares(num), num) for num in arr]
    counts.sort(key=lambda x: (-x[0], x[1]))
    return [num for _, num in counts]


# Примеры использования
print(sort_by_perfsq([715, 112, 136, 169, 144]))  # => [169, 144, 112, 136, 715]
print(sort_by_perfsq([234, 61, 16, 441, 144, 728]))  # => [144, 441, 16, 61, 234, 728]
