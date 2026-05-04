import sys

def check(arg,i):
    if arg > 0:
        return
    elif arg == 0:
        print(f"Аргумент {i + 1} не может равнятся 0")
        sys.exit()
    elif arg < 0:
        print(f"Аргумент {i + 1} не может быть меньше 0")
        sys.exit()
    else:
        print(f"Непредвиденная ошибка в аргументе {i + 1}")
        sys.exit()

def path(n, m, num): #Расчет и вывод пути с использование рекурсии
    print(num,end='')          #end используется что бы строка не переносилась
    num += m - 1
    if num > n:
        num -= n
    if num == 1:
        return
    path(n, m, num)

if len(sys.argv) != 5:
    print("Для запуска программы требует 4 аргумента, n и m для двух массивов означающих размер массива и шаг обхода например:\n6 3 5 4\nГде n1 = 6, m1 = 3, n2 = 5, m2 = 4")
    sys.exit()
for arg in sys.argv[1:]:
    try:
        check(int(arg), sys.argv.index(arg))
    except ValueError:
        print(f"Аргумент {sys.argv.index(arg)} не может содержать буквы")
for i in range(2):
    path(int(sys.argv[i*2+1]),int(sys.argv[i*2+2]),1)

