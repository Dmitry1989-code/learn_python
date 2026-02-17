n, m = map(int, input("Введите два числа через пробел: ").split())

res = []
while n <= m:
    res.append(pow(n, 2))
    n += 1
print(*res)
