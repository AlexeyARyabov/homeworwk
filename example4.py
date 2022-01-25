max = 0
n = int(input("input number: "))
while n > 0:
    d = n % 10
    if d >= max:
        max = d
    n = n // 10
print(max)