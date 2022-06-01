l = [2, 3, 4, 5, 6]
for i in range(int((len(l) + 1) / 2)):
    print(l[i] * l[-(i+1)], end = ' ')

