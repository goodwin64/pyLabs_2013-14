# Эта программа и все дальнейшие на языке Питон 3.3

# назва курсу - Вступ до програмування
# номер лабораторної роботи - №3
# ваше ім’я та прізвище -Донченко Максим
# номер Вашої заліковки - ФЕ-3106

# З бібліотеки "математика" імпортуємо все:
from math import *

# У першому рядку виводитиметься назва курсу та номер заліковки
print ('Вступ до програмування, ФЕ-3106')

# У другому Прізвище, ім"я та номер лаби
print ('Донченко Максим, лаба 3')

# Змінним a, b, c присвоюються float (дійсні)
# значення, введені з клавіатури:
a=float(input('Введіть а: '))
b=float(input('Введіть b: '))
c=float(input('Введіть c: '))

# Враховуємо ОДЗ: (1 варіант)
if a == 3:
    print ('lol, znamennyk 1 drobi raven 0')
elif c == 0:
    print ('haha, znamennyk 2 drobi raven 0')

y= ( sin(2*a) ) / (a-3) + ( atan(b) ) / c
print ('y=', y)
