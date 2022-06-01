l = [1.1, 1.2, 3.1, 5, 10.01]
print(l)
def differ(lis):
    max = 0
    min = 1
    for i in l:
        if max < i % 1: 
            max = i % 1
        if min > i % 1:
            min = i % 1
    print(f'{max} {min}')
    return((max - min))
print(differ(l))
