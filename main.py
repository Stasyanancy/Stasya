def sum(n1,n2):
    return int(n1)+int(n2)


def sub(n1,n2):
    return int(n1)-int(n2)


def mul(n1,n2):
    return int(n1)*int(n2)


def div(n1,n2):
    return int(n1)/int(n2)


def main_menu():
    print('Хотите провести вычесление?')
    wish = input ('')
    while wish=='да':
        symbol = input('Введите знак: ')
        n1 = input('Введите первое число: ')
        n2 = input('Введите второе число: ')
        if symbol=='/'and n2 =='0':
            print('Делить на ноль нельзя!')
        elif symbol == '+':
            print('Результат:', sum(n1,n2))
        elif symbol == '-':
            print('Результат:', sub(n1,n2))
        elif symbol == '*':
            print('Результат:', mul(n1,n2))
        elif symbol == '/':
            print('Результат:', div(n1,n2))
        else:
            print('Ошибка вычисления.')
        print('Хотите считать дальше?')
        wish = input('')
    else:
        print('Конец вычислений.')


main_menu()