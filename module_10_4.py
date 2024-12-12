# импорт необходимых библиотек
import time
from threading import Thread
from queue import Queue
from time import sleep
from random import randint


class Table:
    """ Объявление класса Table. Обладает атрибутами number - номер стола
        и guest - гость, который сидит за этим столом (по умолчанию None)"""

    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    """ Класс Guest наследуется от класса Thread. Обладает атрибутом name - имя гостя.
    Обладает методом run, где происходит ожидание случайным образом от 3 до 10 секунд"""

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))



class Cafe():
    """ Класс Cafe. Объекты этого класса должны создаваться следующим
        способом - Cafe(Table(1), Table(2), ...). Обладает атрибутами
        queue - очередь (объект класса Queue) и tables - столы в этом
        кафе (любая коллекция)"""

    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):  # Метод принимает неограниченное кол-во гостей
        for guest in guests:  # цикл гостя
            for table in self.tables:  # цикл столов
                # условие проверки свободного стола и посадка гостя за стол (назначать
                # столу guest), запуск поток гостя
                if table.guest is None:
                    table.guest = guest
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    table.guest.start()
                    break
            else:  # Свободных столов для посадки нет. Помещаем гостя в очередь queue
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):  # Метод имитирует процесс обслуживания гостей
        """ Цикл обслуживания. Должно происходить пока очередь не пустая (метод empty)
            или хотя бы один стол занят."""
        while (not self.queue.empty()) or (not (t.guest for t in self.tables)):
            for table in self.tables:  # цикл перебора столов
                """ очередь ещё не пуста (метод empty) или один из столов освободился (None), то
                    текущему столу присваивается гость взятый из очереди (queue.get())"""
                if (not self.queue.empty()) and (table.guest is None):
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()  # запустить поток этого гостя
                """ Условие наличия за столом гостя (поток) и гость (поток) закончил
                    приём пищи (поток завершил работу - метод is_alive)"""
                if (not table.guest is None) and (table.guest.is_alive()):
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None  # текущий стол освобождается


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
