from ctypes import c_uint


def add(mas, i, prompt_type): #Проверка вводимых значений с использование рекурсии
    if prompt_type == 0:
        prompt = f"Введите размер массива {i + 1} \n"
    else:
        prompt = f"Введите шаг перебора массива {i + 1} \n"
    try:
        mas.append(int(input(prompt)))
    except ValueError:
        print("Значение не может содержать буквы")
        add(mas, i, prompt_type)
    if(mas[i] == 0):
        print("Значение не может равнятся 0")
        mas.remove(mas[i])
        add(mas, i, prompt_type)
    if (mas[i] < 0):
        print("Значение не может быть меньше 0")
        mas.remove(mas[i])
        add(mas, i, prompt_type)
    return mas

def path(n, m, num): #Расчет и вывод пути с использование рекурсии
    print(num,end='')          #end используется что бы строка не переносилась
    num += m - 1
    if num > n:
        num -= n
    if num == 1:
        print()
        return
    path(n, m, num)



total_mas = 2 #Колличество массивов
n = [] #Размер массива
m = [] #Шаг
for i in range(total_mas):
    add(n,i,0)
    add(m,i,1)
for mas in range(total_mas):
   print(f"Путь для массива {mas+1}")
   path(n[mas],m[mas],1)

