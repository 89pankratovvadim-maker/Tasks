import sys
import math

if len(sys.argv) != 2:
    print("Для работы программы необходимо передать имя файла с массивом")
    sys.exit()

sum_num = 0
steps = 0
nums = []

try:
    nums_file = open(sys.argv[1], 'r')
except FileNotFoundError:
    print(f"Файл {sys.argv[1]} не найден")
    sys.exit()
except PermissionError:
    print(f"Недостаточно прав для доступа к файлу {sys.argv[1]}")
    sys.exit()

for line in nums_file:
    nums.append(int(line))
nums_file.close()

for i in range(len(nums)):
    sum_num += nums[i]
sum_num /= 4
sum_num = math.ceil(sum_num)

for i in range(len(nums)):
    steps += abs(nums[i] - sum_num)
if steps < 20:
    print(steps)
else:
    print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
