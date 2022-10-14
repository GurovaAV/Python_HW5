# Добавьте игру против бота

import random

first_step = int(input("Выберите: орёл (1) или решка (2): ")) 
first_step_coin = int(random.randint(1,2))
print(f'Бросаем монетку... Это - {first_step_coin}')

rest_of_candies = 2021

if first_step != first_step_coin:
    print("Вы не угадали :(  В ящике 2021 конфета. И ходит Бот!")
    while rest_of_candies > 0:
        if rest_of_candies < 28:
            bot_takes_candies = int(random.randint(1,rest_of_candies))
            print(f'Бот взял {bot_takes_candies} конфет')
            rest_of_candies -= bot_takes_candies
            print(f'Конфет осталось: {rest_of_candies}')
            if rest_of_candies == 0:
                print("Конец игры! Бот выиграл!")
                break
            print("*****Переход хода*****")
            candy = int(input("Сколько возьмёте конфет: "))
            rest_of_candies -= candy
            print(f'Конфет осталось: {rest_of_candies}')
            if rest_of_candies == 0:
                print("Конец игры! Вы выиграли!")
                break
            print("*****Переход хода к боту*****")
        else:
            bot_takes_candies = int(random.randint(1,28))
            print(f'Бот взял {bot_takes_candies} конфет')
            rest_of_candies -= bot_takes_candies
            print(f'Конфет осталось: {rest_of_candies}')
            print("*****Переход хода*****")
            candy = int(input("Сколько возьмёте конфет: "))
            rest_of_candies -= candy
            print(f'Конфет осталось: {rest_of_candies}')
            print("*****Переход хода к боту*****")

else:
    print("Вы угадали! Итак, в ящике 2021 конфета. Ходите!")
    while rest_of_candies > 0:
        if rest_of_candies < 28:
            bot_takes_candies = int(random.randint(1,rest_of_candies))
            print(f'Бот взял {bot_takes_candies} конфет')
            rest_of_candies -= bot_takes_candies
            print(f'Конфет осталось: {rest_of_candies}')
            if rest_of_candies == 0:
                print("Конец игры! Бот выиграл!")
                break
            print("*****Переход хода*****")
            candy = int(input("Сколько возьмёте конфет: "))
            rest_of_candies -= candy
            print(f'Конфет осталось: {rest_of_candies}')
            if rest_of_candies == 0:
                print("Конец игры! Вы выиграли!")
                break
            print("*****Переход хода к боту*****")
        else:
            candy = int(input("Сколько возьмёте конфет: "))
            rest_of_candies -= candy
            print(f'Конфет осталось: {rest_of_candies}')
            if rest_of_candies == 0:
                print("Конец игры!")
                break
            print("*****Переход хода к боту*****")
            bot_takes_candies = int(random.randint(1,28))
            print(f'Бот взял {bot_takes_candies} конфет')
            rest_of_candies -= bot_takes_candies
            print(f'Конфет осталось: {rest_of_candies}')
            if rest_of_candies == 0:
                print("Конец игры!")
                break
            print("*****Переход хода*****")
