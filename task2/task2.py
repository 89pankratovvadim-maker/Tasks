import sys
import re

if len(sys.argv) != 3:
    print("Для работы программы нужно предать 2 аргумента\n1. Имя файла с координатами и размером круга\n2. Имя файла с координатами точек")
    sys.exit()

try:
    file_read = open(sys.argv[1], 'r')
except FileNotFoundError:
    print(f"Файл {sys.argv[1]} не найден")
    sys.exit()
except PermissionError:
    print(f"Недостаточно прав для доступа к файлу {sys.argv[1]}")
    sys.exit()
line = file_read.readline()
x = float(re.findall(r'\d+', line)[0])
y = float(re.findall(r'\d+', line)[1])
line = file_read.readline()
a = float(re.findall(r'\d+', line)[0])
b = float(re.findall(r'\d+', line)[1])
file_read.close()
if x > 10**-38 and y > 10**-38 and x < 10**38 and y < 10**38:
    pointx = []
    pointy = []

    try:
        file_read = open(sys.argv[2], 'r')
    except FileNotFoundError:
        print(f"Файл {sys.argv[2]} не найден")
        sys.exit()
    except PermissionError:
        print(f"Недостаточно прав для доступа к файлу {sys.argv[2]}")
        sys.exit()
    count = 0
    for line in file_read:
        count += 1
    if count == 0:
        print("Нужна минимум 1 точка")
        file_read.close()
        sys.exit()
    if count > 100:
        print("Максимальное количество точек не может быть больше 100")
        file_read.close()
        sys.exit()
    file_read.seek(0)
    for line in file_read:
        if float(re.findall(r'\d+', line)[0]) > 10 ** -38 and float(re.findall(r'\d+', line)[1]) > 10 ** -38 and float(re.findall(r'\d+', line)[0]) < 10 ** 38 and float(re.findall(r'\d+', line)[1]) < 10 ** 38:
            pointx.append(float(re.findall(r'\d+', line)[0]))
            pointy.append(float(re.findall(r'\d+', line)[1]))
        else:
            print("Координаты точки должны находится в диапазоне от 10^-38 и 10^38")
            sys.exit()
    file_read.close()

    for i in range(len(pointx)):
        pos_type = ((pointx[i] - x) * (pointx[i] - x)) / ((a) * (a)) + ((pointy[i] - y) * (pointy[i] - y)) / ((b) * (b))
        if pos_type == 1:
            print("0")
        if pos_type < 1:
            print("1")
        if pos_type > 1:
            print("2")
else:
    print("Координаты должны находится в диапазоне от 10^-38 и 10^38")
    sys.exit()

