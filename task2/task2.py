import re

circle_path = 'Circle.txt'
dots_path = 'Dots.txt'

file_read = open(circle_path, 'r')
line = file_read.readline()
x = float(re.findall(r'\d+', line)[0])
y = float(re.findall(r'\d+', line)[1])
line = file_read.readline()
a = float(re.findall(r'\d+', line)[0])
b = float(re.findall(r'\d+', line)[1])
file_read.close()

if x < 10^-38 or y < 10^-38:
    print("Координата не может быть меньше 10^-38")
    exit()
if x > 10^38 or y > 10^38:
    print("Координата не может быть больше 10^38")
    exit()

pointx = []
pointy = []

file_read = open(dots_path, 'r')
count = 0
for line in file_read:
    count +=1
if count == 0:
    print("Нужна минимум 1 точка")
    exit()
if count > 100:
    print("Максимальное количество точек не может быть больше 100")
    exit()
file_read.seek(0)
for line in file_read:
    pointx.append(float(re.findall(r'\d+', line)[0]))
    pointy.append(float(re.findall(r'\d+', line)[1]))
file_read.close()

for i in range(len(pointx)):
    pos_type = ((pointx[i]-x)*(pointx[i]-x))/((a)*(a))+((pointy[i]-y)*(pointy[i]-y))/((b)*(b))
    if pos_type == 1:
        print("0")
    if pos_type < 1:
        print("1")
    if pos_type > 1:
        print("2")