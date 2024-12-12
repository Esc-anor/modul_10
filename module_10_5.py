# импорт необходимых библиотек
import multiprocessing
from datetime import datetime


def read_info(name):                 # объявление функции чтения файлов
    all_data = []                    # создание локального списка
    with open(name, 'r') as f:       # открытие файла на чтение
        while True:                  # цикл считывания файла построчно
            line = f.readline()      # считывание строки
            all_data.append(line)    # добавление считанной строки в конец списка
            if not line:             # прерываем цикл, если строка пустая
                break


if __name__ == '__main__':
    # Линейный вызов
    files = [f'./file {number}.txt' for number in range(1, 5)]      # переменная списка файлов
    st1 = datetime.now()                          # фиксация времени начала линейной обработки
    for f in files:                               # цикл чтения списка файлов
        read = read_info(f)    # обращение к функции read_info для обработки файла f из files
    print(f'линейного вызов: {datetime.now() - st1}')

    # Многопроцессный
    st2 = datetime.now()  # фиксация времени начала мультипроцессорной обработки
    with multiprocessing.Pool(processes=4) as pool:  # обращение к мультипроцессорному методу
        pool.map(read_info, files)  # передача данных в мультипроцессорный метод

    print(f'мультипроцесс: {datetime.now() - st2}')
