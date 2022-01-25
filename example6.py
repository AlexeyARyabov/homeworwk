r = int(input("input revenue: "))
c = int(input("input charge: "))
if r > c:
#расчет рентабельности
    prof = (r - c) / r
   #прибыль на одного сотрудника
    n = int(input("input number of employees: "))
    k = prof / n
    print('you profit: ', prof)
    print('you profit per employee: ', k)
else:
    print('you are at a loss')