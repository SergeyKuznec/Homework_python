n = int(input('введите число в 10 степени счисления'))
b = ''
while n > 0:
    b = str(n % 2) + b
    n = n // 2
print(b)