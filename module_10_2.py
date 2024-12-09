from threading import Thread  # импорт из модуля threading класса Thread для создания потока(ов)
from time import sleep  # импорт из модуля time функции sleep


class Knight(Thread):  # объявление класса Knight наследованного от Thread
    def __init__(self, name, power):  # метод инициализации героя в классе
        self.knight = name  # имя рыцаря. (str)
        self.power = power  # сила рыцаря. (int)
        super().__init__()  # обращение к родительскому классу Thread

    def run(self):  # метод реализации битвы с врагами
        print(f'{self.knight}, на нас напали!')
        enemy = 100  # объявление количества врагов
        day = 0  # объявление начала битвы с врагами
        while enemy > 0:  # цикл while проверки остатка врагов и количества дней битвы
            enemy -= self.power  # уменьшение количества врагов в зависимости от силы героя
            day += 1  # увеличение количества дней битвы
            sleep(1)  # пауза выполнение цикла
            print(f'{self.knight}, сражается {day} день(дня)..., осталось {enemy} воинов')
        print(f'{self.knight} одержал победу спустя {day} дней(дня)!')  # Враги закончились


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print('Все битвы закончились!')
