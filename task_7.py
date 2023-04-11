def hello(f):
    def name():
        name_1 = input('Введите имя: ')
        return f() + name_1
    return name
@hello
def res():
    return 'Привет,'

print(res())