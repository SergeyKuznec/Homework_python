n = int(input('введите число n '))
sum = 0
diction = {}
for i in range(1, n+1):
    sum += (1+1/i)**i
    diction[i] = (1+1/i)**i
    ##print((1+1/i)**i, end = ' ')
print(diction)
print('сумма равна ', sum)
