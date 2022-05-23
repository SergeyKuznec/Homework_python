number = int(input('введите день недели '))
if number == 6 or number == 7:
    print("Weekend")
elif 1 <= number <= 5:
    print("Weekday")
else:
    print("wrong number")
