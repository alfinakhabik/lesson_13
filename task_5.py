def countdown():
    l = [i for i in range(0, 11)]
    s = list(reversed(l))
    for i in s:
        if i == 0:
            s.append('Пуск!')
    return s
print(countdown())