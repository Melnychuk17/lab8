# прямий пошук підрядка
# Мельничук Олена 122В

# виводимо рядок на екран
list='It’s never too late to be what you might have been'
print(list)
# вводимо підрядок
list1=input('Enter substring  ')
i=-1   # індекс рядка
j=0   # індекс підрядка
while (j<len(list1)) and i<(len(list)-len(list1)):
    j=0
    i+=1   #к-сть зміщень
    while j<len (list1) and list1[j]==list[i+j]:
        j+=1
if (j==len(list1)):
    print(f'Item found at position  {i}, for {i} displacements')
else:
    print('Substring not found')