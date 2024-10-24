a = [10, -3, -5, 2, 5]
index = 0
b = min(a)
for i in a:
    if i == b:
        print(index)
        break
    index += 1
