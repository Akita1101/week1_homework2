str_input = input("データを入力してください(スペース区切り) > ")

str_numbers = str_input.split()

numbers = []

for number_str in str_numbers:
    numbers.append(int(number_str))


def total_value(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def max_value(numbers):
    maximum = max(numbers)
    return maximum


def min_value(numbers):
    minimum = min(numbers)
    return minimum


def avg_value(numbers):
    total = total_value(numbers)
    average = total / len(numbers)
    return int(average)


print(f"合計値: {total_value(numbers)}")
print(f"最大値: {max_value(numbers)}")
print(f"最小値: {min_value(numbers)}")
print(f"平均値: {avg_value(numbers)}")
