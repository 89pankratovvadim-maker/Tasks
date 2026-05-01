import re

values_path = ('values.json')
tests_path = ('tests.json')
report_path = ('report.json')

values_file = open(values_path, 'r') #Чтение файла с результатами и сохранение их в два массива с id и результатами
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

report_file = open(report_path, 'w') #Чтение файла и запись с добавлеными результатами
test_file = open(tests_path, 'r')
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