'''
С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
Задайте список из нескольких чисел. 
Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
'''
lst = []
lst = list(map(int, input('Введите несколько чисел: ').split()))
def summaOdd(lst):
    countSum = 0
    for i in range(len(lst)):
        if i%2 != 0:
            countSum+=lst[i]
    print(countSum)

summaOdd(lst)