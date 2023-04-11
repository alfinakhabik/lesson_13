a = input('Введите предложение, которое хотите расшифровать: ')
def cesar(s, k):
    d = ""
    for i in s:
        if i.isupper():
            index = ord(i) - ord('А')
            g = (index - k) % 32 + ord('А')
            o = chr(g)
            d += o
        elif i.islower():
            index = ord(i) - ord('а')
            g = (index - k) % 32 + ord('а')
            o = chr(g)
            d += o
        else:
            d += i
    return d

print(cesar(a, 3))