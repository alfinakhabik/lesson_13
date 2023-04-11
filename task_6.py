# a)
def alphabet():
    for i in range(65, 91):
        print(f'Порядковый номер буквы {chr(i)}: {ord(chr(i)) - ord(chr(65)) + 1}')

alphabet()

# б)
def alphabet_1():
    bukvi = []
    for i in range(65, 91):
        bukvi.append(chr(i))
    nomera = []
    for i in range(65, 91):
        nomera.append(ord(chr(i)) - ord(chr(65)) + 1)
    Mydict = {nomera[i]: bukvi[i] for i in range(0, len(nomera), 1)}
    print(Mydict)

alphabet_1()