def my_func(x, y):
    if x > 0 and isinstance(x, float) and isinstance(y, int) and (y < 0):
        #return x ** y """возведение в степень с помощью оператора **"""
        """реализация без оператора **, с использованием цикла"""
        i= 1
        res= 1
        while i <= abs(y):
            res *= x
            i +=1
        return 1 / res
    else:
        return 'Одно или оба числа не удовлетворяют условию задачи'


print(my_func(2, -4))
