import sys
import re

if len(sys.argv) != 4:
    print("Программа должна содержать 3 аргумента\n1. Имя json файла с результатами теста\n2. Имя json файла со структурой тестов\n3. Имя json файла в который будет записан результат")
    sys.exit()

try:
    values_file = open(sys.argv[1], 'r') #Чтение файла с результатами и сохранение их в два массива с id и результатами
except FileNotFoundError:
    print(f"Файл {sys.argv[1]} не найден")
    sys.exit()
except PermissionError:
    print(f"Недостаточно прав для доступа к файлу {sys.argv[1]}")
    sys.exit()
test_id = []
test_values = []
for line in values_file:
    if '"id"' in line:
        test_id.append(re.findall(r'\d+', line))
    if '"passed"' in line:
        test_values.append('"passed"')
    if '"failed"' in line:
        test_values.append('"failed"')
values_file.close()

try:
    report_file = open(sys.argv[3], 'w') #Запись с добавлеными результатами
except:
    print(f"Не удалось создать файл {sys.argv[3]}")
    sys.exit()

try:
    test_file = open(sys.argv[2], 'r')
except FileNotFoundError:
    print(f"Файл {sys.argv[2]} не найден")
    sys.exit()
except PermissionError:
    print(f"Недостаточно прав для доступа к файлу {sys.argv[2]}")
    sys.exit()

for line in test_file:
    if '"id"' in line:
        if re.findall(r'\d+', line) in test_id:
            id = test_id.index(re.findall(r'\d+', line))
        else:
            id = -1
    if '"value"' in line:
        if id != -1:
            line = line.replace('""',test_values[id])
    report_file.write(line)
report_file.close()
test_file.close()