def tetration(tet, a):
    s=1
    for i in range(tet):
        s=a**s
    return len(str(s))
print(tetration(3,5))
print(tetration(5,2))
