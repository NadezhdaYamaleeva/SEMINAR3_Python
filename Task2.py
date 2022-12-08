# Напишите программу, которая найдет произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] -> [12, 15, 16];
# - [2, 3, 5, 6] -> [12, 15]

spisok1 = [int(I) for I in input('Введите числа: ').split()]
print(spisok1)
spisok2 = []
flag1 = len(spisok1)
for i in range(len(spisok1)):
    while i < len(spisok1)/2 and flag1 > len(spisok1)/2:
        flag1 = flag1 - 1
        a = spisok1[i] * spisok1[flag1]
        spisok2.append(a)
        i += 1
print(spisok2)