# виконайте добуток двох квадратних матриць 3*3, врахуйте розмірність.
# Результати множення елементів занесіть до нової матриці та виведіть її на екран
# Мельничук Олена 122В

# імпортуємо бібліотеку numpy
import numpy as np
# створюємо пусту змінну і два пустих списка для значень
dop=[]
matrix3=[]
z=0
while True:
    # розмірність першої матриці
    n,m=int(input('Enter the number of lines1:  ')), \
        int(input('Enter the number of columns1: '))
    # розмірність другої матриці
    a,b=int(input('Enter the number of lines2:  ')), \
        int(input('Enter the number of columns2: '))
    # перевірка розмірності 3 на 3
    while n !=3 or m !=3:
        n,m=int(input('Enter the number of lines1:  ')), \
            int(input('Enter the number of columns1: '))
        a,b=int(input('Enter the number of lines2:  ')), \
            int(input('Enter the number of columns2: '))

    # ініціалізуємо елементи нулем заданого типу даних і вказуємо що це int
    matrix1=np.zeros((n,m),dtype=int)
    matrix2=np.zeros((a,b),dtype=int)
    # елементи в рядках і стовпцях 1 матриці
    for i in range(n):
        for j in range(m):
            # заповнюємо 1 матрицю
            matrix1[i,j]=int(input(f'M1[{i+1},{j+1}]='))
    # елементи в рядках і стовпцях 2 матриці
    for x in range(a):
        for y in range(b):
            # заповнюємо 2 матрицю
            matrix2[x,y]=int(input(f'M2[{x+1},{y+1}]='))
    print('Matrix 1')
    print(matrix1)
    print('Matrix 2')
    print(matrix2)
    # множення матриць 1 і 2
    for i in range(n):  # рядки 1 матриці
        for y in range(b):  # стовпці 2 матриці
            for j in range(m):  # стовпці 1 матриці
                z=z+matrix1[i][j]*matrix2[j][y]
            # добавляємо значення в список
            dop.append(z)
            ro=0
        # записуємо значення у фінальний список
        matrix3.append(dop)
        dop=[]
    print(f'Matrix 3 {matrix3}')
    # запит на виконання програми ще раз
    result = input('Want to restart? If yes - 1, no - other: ')
    if result == '1':
        continue
    else:
        break

