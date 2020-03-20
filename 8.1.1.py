# виведіть на екран елементи лінійного масиву (заданий користувачем) у
# зворотному порядку
# Мельничук Олена 122В

# імпортуємо бібліотеку numpy
import numpy as np
# зациклюємо програму
while True:
    while True:
        try:
            # вводимо скільки елементів має містити матриця
            x = int(input('Enter number of matrix elements: '))
            break
        # якщо х не число, просимо ввести ще раз поки не буде число
        except ValueError:
            print('Enter number: ')

    # ініціалізуємо елементи нулем заданого типу даних і вказуємо що це int
    matrix = np.zeros(x, dtype=int)
    n = []    # пустий список для масиву
    # на місця елементів матриці вводимо наші знацення числового типу
    for i in range(x):
        matrix[i] = int(input('Enter your element: '))
    # тепер елементи нашої матриці ставимо в зворотньому порядку
    for j in range(x):
        q = matrix[x - 1 - j]
        # добавляємо в список
        n.append(q)
        # Виводимо нашу матрицю
    print(n)
    # запит на виконання програми ще раз
    result = input('Want to restart? If yes - 1, no - other: ')
    if result == '1':
        continue
    else:
        break











