"""На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были 
повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть"""

n = int(input('Введите число монет: '))
count = 0
for i in range(n):
    if int(input()) == 0:
        count+=1
if n - count <count:

    print(n-count)
else:
    print(count)

    