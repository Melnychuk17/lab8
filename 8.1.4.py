# у матриці 4*4, що задана користувачем замініть всі від’ємні елементи на 0.
# Мельничук Олени 122В

# імпортуємо бібліотеку numpy
import numpy as np
# зациклюємо
while True:
    # вводимо розмірність матриці
    n, m = int(input('Enter the number of lines:  ')), \
           int(input('Enter the number of columns: '))
    # перевіряємо чи вона 4 на 4
    while n != 4 or m != 4:
        n, m = int(input('Enter the number of lines:  ')), \
               int(input('Enter the number of columns: '))

    # ініціалізуємо елементи нулем заданого типу даних і вказуємо що це int
    matrix = np.zeros((n, m), dtype=int)
    for i in range(n):  # елементи в рядку
        for j in range(m):  # елементи в стовпці
            # заповнюємо і транспонуємо матрицю
            matrix[i, j] = int(input(f'M[{i + 1},{j + 1}]='))
    print('Matrix')
    print(matrix)
    for i in range(n):  # елементи в рядку
        for j in range(m):  # елементи в стовпці
            # всі від'ємні елементи замінюємо на 0
            if matrix[i, j] < 0:
                matrix[i, j] = 0
    print('New matrix')
    print(matrix)
    # запит на виконання програми ще раз
    result = input('Want to restart? If yes - 1, no - other: ')
    if result == '1':
        continue
    else:
        break