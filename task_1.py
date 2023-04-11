z=input('Введите знак операции: ')
a=int(input('Введите первое число: '))
b=int(input('Введите второе число: '))
def calculate(z1,a1,b1):
        if z1 == '*':
            print(eval(f'{a1}{z1}{b1}'))
        elif z1 == '+':
            print(eval(f'{a1}{z1}{b1}'))
        elif z1 == '-':
            print(eval(f'{a1}{z1}{b1}'))
        elif z1 == '/':
            if b1 != 0:
                print(eval(f'{a1}{z1}{b1}'))
            else:
                print('На ноль делить нельзя!')
calculate(z, a, b)