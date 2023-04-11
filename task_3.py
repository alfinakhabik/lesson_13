def honest(n):
    return n % 2 == 0

n_1 = [i for i in range(0, 21)]
print(*filter(honest, n_1))