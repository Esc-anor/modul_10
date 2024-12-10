import threading
import random
import time
from threading import Thread, Lock


class Bank(Thread):

    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()

    # 1-й Поток "Пополнение"
    def deposit(self):
        for i in range(100):  # 100 транзакций пополнения средств
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            y = random.randint(50, 500)
            self.balance += y  # Пополнение на случайное целое число от 50 до 500
            print(f'Пополнение: {y}. Баланс: {self.balance}')
            time.sleep(0.001)  # ожидание в 0.001 секунды, имитация скорости выполнения пополнения.

    # 2-й поток "Снятие"
    def take(self):
        for i in range(100):  # 100 транзакций снятия средств
            x = random.randint(50, 500)
            print(f'Запрос на {x}')
            if self.balance >= x:
                self.balance -= x  # Снятие на случайное целое число от 50 до 500
                print(f'Снятие: {x}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()  # Если 'x' оказалось больше баланса, то заблокировать поток методом acquire.
            time.sleep(0.001)


bk = Bank()
# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')