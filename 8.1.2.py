# виведіть на екран транспоновану матрицю 3*3 (початкова матриця задана користувачем).
# Мельничук Олени 122В

# імпортуємо бібліотеку numpy
import numpy as np
# зациклюємо
while True:
    # вводимо розмірність матриці
    n, m = int(input('Enter the number of lines:  ')), \
           int(input('Enter the number of columns: '))
    # перевіряємо чи вона 3 на 3
    while n != 3 or m != 3:
        n, m = int(input('Enter the number of lines:  ')), \
               int(input('Enter the number of columns: '))

    # ініціалізуємо елементи нулем заданого типу даних і вказуємо що це int
    matrix = np.zeros((n, m), dtype=int)
    for i in range(n):  # елементи в рядку
        for j in range(m):  # елементи в стовпці
            # заповнюємо і транспонуємо матрицю
            matrix[i, j] = int(input(f'A[{j + 1},{i + 1}]='))
    print('The transposed matrix')
    print(matrix)
    # запит на виконання програми ще раз
    result = input('Want to restart? If yes - 1, no - other: ')
    if result == '1':
        continue
    else:
        break