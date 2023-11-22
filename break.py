while True:
    name = input("enter your name: ")
    if name != "a":
        break
    else:
        print(name)
phone = "123-214-3245"
for i in phone:
    if i == "-":
        continue
    print(i, end="")
for i in range(1, 21):

    if i != 13:
        pass
    else:

        print(i)
