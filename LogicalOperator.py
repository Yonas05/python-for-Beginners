temp = int(input("What is the temperature Outside"))
if 0 < temp < 30:
    print("the temperature is good today !")
    print("go outside")
elif temp < 0 or temp > 30:
    print("the temperature is bad today")
 