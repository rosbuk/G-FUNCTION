"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию


year = input('Ввведите год рождения А.С.Пушкина:')
while year != '1799':
    print("Не верно")
    year = input('Ввведите год рождения А.С.Пушкина:')
print('Верно')

day = input('В какой день июня родился Пушкин?')
while day != '6':
    print("Не верно")
    day = input('В какой день июня родился Пушкин?')
print('Верно')

"""


pushkin_born = {'answere' : ['год', 'месяц', 'день'],
                'ask' : ['Ввведите год рождения А.С.Пушкина: ', 'В каком месяце родился Пушкин? ', 'В какой день июня родился Пушкин? '],
                'right_answere' : ['1799', 'В июне', '6']
}

def pushkin(i):
    pushkin_born['answere'][i] = input(pushkin_born['ask'][i])
    while pushkin_born['answere'][i] != pushkin_born['right_answere'][i]:
        print("Не верно")
        pushkin_born['answere'][i] = input(pushkin_born['ask'][i])
    print('Верно')

for i in range(3):
    pushkin(i)