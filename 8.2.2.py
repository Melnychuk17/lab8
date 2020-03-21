# Бінарний пошук
# Мельничук Олена 122В

import numpy as np
# створюємо масив для перевірки
m1=np.array(range(1,21))
print(m1)
# Вводимо якийсь елемент для пошуку
x=int(input('Enter the element '))
d=len(m1)-1  # кінець масиву
# вводимо лічильник підрахунку ітерацій
n,count,a=0,0,0,  # початок масиву, лічильник
flag=False
while n<=d and not flag :
    a=(n+d)//2
    count+=1
    if m1[a]==x:
        flag=True
    elif m1[a]<x:
        count += 1
        n=a+1
    else:
        count += 1
        d=a-1
if not flag:
    print('There is no item')
else:
    print(f'Item found at position {a} at {count} comparison')