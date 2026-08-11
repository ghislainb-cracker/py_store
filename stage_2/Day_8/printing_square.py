rows = int(input("Enter number of rows you want? "))
columns = int(input("Enter number of columns of you want? "))
sign = input("What sign will you be using? ")

for x in range(rows):
    for y in range(columns):
        print(sign, end=" ")
    print()