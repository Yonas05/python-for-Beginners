def add(*stuff):
    sum = 0

    stuff = list(stuff)
    stuff[9] = 100
    for i in stuff:
        sum += i
    return sum


print(add(2, 4, 7, 4, 5, 6, 4, 6, 2, 7, 3))
