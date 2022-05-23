x, y = int(input('введите координату Х ')), int(input('введите координату Y '))
if x > 0 and y > 0:
    print("1 плоскость")
elif x < 0 and y > 0:
    print("2 плоскость")
elif x < 0 and y < 0:
    print("3 плоскость")
elif x > 0 and y < 0:
    print("4 плоскость")
