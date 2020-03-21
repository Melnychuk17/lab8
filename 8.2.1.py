# Мельничук Олена 122В
# Лінійний пошук

import random
import numpy as np
# створюємо масив для перевірки
m1=np.array(range(1,21))
print(m1)
# Вводимо якийсь елемент для пошуку
x=int(input('Enter the element '))
d=len(m1)
# вводимо лічильник підрахунку ітерацій
count=0
q=0
# вводимо лінійний пошук
# кількість порівнянь повина бути на 1 менше кількості значень в задачі
# якщо к-сть порівнянь = кількості значень, то такого елемента немає
while q<d and m1[q]!=x:
    q+=1
    count+=2
print('Number of comparisons ',count)
if q==d:
    print('There is no item')
else:
    print(f'On position {q} found {x}')
# з рандомними значеннями
# ініціалізуємо елементи нулем заданого типу даних і вказуємо що це int
m2=np.zeros(20,dtype=int)
for i in range(20):
    m2[i]=random.randint(-10,5)
print(m2)
d1=len(m2)
count2=0
v=0
# вводимо лінійний пошук
while v<d and m2[v]!=x:
    v+=1
    count2+=2
print('Number of comparisons',count2)
if v==d1:
    print('There is no item')
else:
    print(f'On position {v} found {x}')
