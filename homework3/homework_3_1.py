def div(a, b):
    if b!=0:
        return a / b
    else:
        return 'Делить на 0 нельзя!. Введи другое число'


print(div(int(input('введите делимое: ')), int(input('введите делитель: '))))
