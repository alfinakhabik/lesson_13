s = ['анТОн', 'НАТАЛЬЯ', 'никита', 'МаРиЯ', '!СЕРГЕЙ!', 'Владимир747', 'Павел+100500']

def imena(names):
    name = ''.join(filter(str.isalpha, names))
    name = name.capitalize()
    return name
imena_1 = list(map(imena, s))
print(imena_1)