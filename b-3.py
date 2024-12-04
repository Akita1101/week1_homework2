column_number = int(input("行数を入力してください:"))
row_number = int(input("列数を入力してください:"))
for column in range(1, column_number + 1):
    for row in range(1, row_number + 1):
        result = column * row
        print(f" {column} * {row} = {result: >2} |", end="")
    print("")
