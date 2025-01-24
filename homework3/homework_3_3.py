def sum_max(*args):
    my_sum = 0
    my_list = list(args)
    while len(my_list) > 1:
        s_max = max(my_list)
        my_sum += s_max
        my_list.remove(s_max)
    return my_sum


print(sum_max(12, 3, 6))
