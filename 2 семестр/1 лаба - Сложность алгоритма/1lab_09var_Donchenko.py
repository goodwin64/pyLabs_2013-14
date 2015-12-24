# 9. Дан список заполненный строками, где некоторые
# строки могут повторяться. Получите отсортированный список,
# в котором не будет содержаться строк, которые повторялись.   

import random

def swap(arr, i, j): # функция, которая меняет 2 элемента местами
    arr[i], arr[j] = arr[j], arr[i]
 
def Sortiruem(arr): # использование "пузырька", при этом сравнивать можно и строки
    i = len(arr)
    while i > 1:
       for j in range(i - 1):
           if arr[j] > arr[j + 1]:
               swap(arr, j, j + 1)
       i -= 1
    

# Размер дальнейшего списка
SizeOfArray=int(input('Введіть розмір подальшого списку - кількість елементів у ньому: '))

# наш список
Array=[]

# аппенд - добавляет к списку на последнюю позицию элемент
for k in range(1, SizeOfArray+1):
    z=input('your fraze: ') # работа random'a только с целыми числами
    Array.append(z)
    
print('Было', len(Array), 'элементов')
print()
print('Неотсортированный список: ', Array)
Sortiruem(Array)
print('Отсортированный список: ', Array)
print()

x=0
while x<len(Array)-1: # ограничение на индекс, чтоб был меньше длины массива
    if Array[x]==Array[x+1]:
        del Array[x]
        x-=1
    x+=1
    
print ('--->', tuple(Array))
print('Стало', len(Array), 'элементов')
            










    
