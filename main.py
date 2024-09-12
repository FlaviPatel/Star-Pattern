row = int(input("Enter the row: "))

for i in range(row):
    for j in range(i + 1):
        print("*", end="")
    print("\n")