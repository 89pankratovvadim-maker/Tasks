import math

sum_num = 0
steps = 0
nums = []
nums_path = ('Nums.txt')

nums_file = open(nums_path, 'r')
for line in nums_file:
    nums.append(int(line))
nums_file.close()

for i in range(len(nums)):
    sum_num += nums[i]
sum_num /= 4
sum_num = math.ceil(sum_num)

for i in range(len(nums)):
    steps += abs(nums[i] - sum_num)
if steps > 20:
    print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
else:
    print(steps)