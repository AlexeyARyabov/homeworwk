def my_sum():
    res_sum = 0
    while True:
        my_list = input('введи числа ').split()
        for el in my_list:
            if el == 'q':
                print(res_sum)
                break
            else:
                res_sum += int(el)

        else:
            print(res_sum)
            continue
        break


my_sum()
