from cmath import sqrt


x1, y1, x2, y2 = int(input("введите координату Х первой точки ")), int(input("введите координату Y первой точки ")), int(input("введите координату Х второй точки ")), int(input("введите координату Y второй точки "))
print("расстояние между 2 точками равно", abs(sqrt((x2-x1)**2 + (y2 - y1)**2)))