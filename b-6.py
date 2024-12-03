import random

number = int(input("サイコロの面の数は?: "))
time = int(input("何回振りますか?: "))
result_list = []
for x in range(time):
    result = random.randint(1, number)
    result_list.append(result)
print(result_list)
