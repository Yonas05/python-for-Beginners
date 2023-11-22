rows = int(input("how many row? :"))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")
for i in range(rows):
    for j in range(columns):
        print(symbol,end=" ")
    print()
