import csv
from datetime import datetime, timedelta
import os
import asyncio
import aiogram.exceptions
import pandas as pd

def add_user_to_table(data_tuples, filename='data/user_data.csv'):
    # Проверяем, существует ли файл и имеет ли он заголовки
    file_exists = os.path.isfile(filename)
    file_empty = os.stat(filename).st_size == 0 if file_exists else True
    existing_ids = set()  # Набор для хранения уже существующих user_id

    # Если файл существует и не пустой, загружаем все существующие user_id для проверки
    if file_exists and not file_empty:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader, None)  # Пропускаем заголовки
            for row in reader:
                existing_ids.add(row[0])  # Предполагаем, что user_id в первом столбце

    # Собираем заголовки и данные из кортежей
    headers = [tup[0] for tup in data_tuples]
    data = [str(tup[1]) if tup[1] is not None else 'None' for tup in data_tuples]

    # Проверяем, существует ли пользователь с данным user_id
    user_id = str(data[0])  # Предполагаем, что user_id в первом столбце данных
    if user_id in existing_ids:
        print(f"User with ID {user_id} already exists. Skipping...")
        return

    # Открываем файл в режиме добавления
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Если файл пустой, добавляем заголовки
        if file_empty:
            writer.writerow(headers)

        # Записываем данные
        writer.writerow(data)


def log_message(message: str, csv_file='data/admin_data.csv'):
    # Определяем заголовки
    headers = ['date', 'admin_msg']
    
    # Проверяем, существует ли файл и есть ли в нем данные
    file_exists = os.path.isfile(csv_file)
    
    if not file_exists or os.stat(csv_file).st_size == 0:
        # Если файл не существует или пустой, добавляем заголовки
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
            writer.writerow(headers)
        print(f"Заголовки добавлены в файл: {csv_file}")

    # Получаем текущую дату и время
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Записываем сообщение в CSV файл
    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        writer.writerow([current_date, message])
    print(f"Сообщение добавлено: {message}")


def get_user_id(filename='data/user_data.csv'):
    user_ids = []
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Пропустить заголовок

            for row in reader:
                user_id = row[0]  # Первый элемент строки (индекс 0)
                user_ids.append(user_id)
    except Exception as e:
        print(f"Error - {e}")
        return None

    return user_ids

def get_recent_messages(csv_file = 'data/admin_data.csv'):
    recent_messages = []
    seven_days_ago = datetime.now() - timedelta(days=7)
    try:
        # Читаем данные из CSV файла
        with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            # Пропускаем заголовки
            next(reader)
            for row in reader:
                # Получаем дату из первого столбца
                message_date = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
                # Проверяем, если дата меньше 7 дней назад
                if message_date >= seven_days_ago:
                    recent_messages.append(row[1])  # Добавляем сообщение из второго столбца

        return recent_messages
    except StopIteration as e:
        print(f"Error - {e}")
        return None


class Messega_data:
    """Data class for storing and updating message ID"""

    def __init__(self, msg_id):
        self.msg_id = msg_id  # Устанавливаем начальный msg_id

    def __setattr__(self, key, value):
        if key == "msg_id":
            super().__setattr__(key, value)  # Обновляем msg_id
        else:
            raise AttributeError(f"Cannot set {key}, only msg_id is allowed")

    def __getattr__(self, item):
        if item == "msg_id":
            return super().__getattribute__(item)  # Возвращаем msg_id
        else:
            raise AttributeError(f"{item} не найдено")

class MessageHistory:
    """Класс для хранения истории сообщений."""

    def __init__(self):
        self._msg_id = 0
        self.messages = {}  # Словарь для хранения сообщений

    def add_message(self, sender, message):
        """Добавляет сообщение в словарь, очищая текст от лишних символов."""
        cleaned_message = message.strip().replace('\n', '')  # Убираем пробелы и символы новой строки
        self.messages[self._msg_id] = {'time': datetime.now() ,
                                       'sender': sender,
                                       'message': cleaned_message}
        self._msg_id += 1  # Увеличиваем msg_id для следующего сообщения

    def get_messages(self):
        """Возвращает все сообщения."""
        temp_output = ""
        for entry in self.messages.values():
            temp_output += f"{entry['time']} - {entry['sender']} написал: {entry['message']}\n"
        return temp_output

    def clear_messages(self):
        """Очищает словарь сообщений."""
        self.messages.clear()
        print("Сообщения очищены.")


class DataStorage:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataStorage, cls).__new__(cls)
            # Инициализация списков при создании экземпляра
            cls._instance.column1 = []
            cls._instance.column2 = []
            cls._instance.column3 = []
            cls._instance.column4 = []
        return cls._instance

    def set_columns(self, col1, col2, col3, col4):
        """Метод для записи данных в списки."""
        self.column1 = col1
        self.column2 = col2
        self.column3 = col3
        self.column4 = col4

    def get_columns(self):
        """Метод для получения данных из списков."""
        return self.column1, self.column2, self.column3, self.column4


class DataStorage_text:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataStorage_text, cls).__new__(cls)
            # Инициализация списков при создании экземпляра
            cls._instance.text_start = ''
            cls._instance.text_buy = ''
            cls._instance.text_expert = ''
        return cls._instance

    def set_texts(self, col1, col2, col3):
        """Метод для записи данных в списки."""
        self.text_start = col1
        self.text_buy = col2
        self.text_expert = col3

    def get_texts(self):
        """Метод для получения данных из списков."""
        return self.text_start, self.text_buy, self.text_expert



# Пример использования
msg_data = Messega_data(msg_id=0)


# delet last msgs
async def delet(clbk):
    previous_msg = msg_data.msg_id
    chat_id = clbk.message.chat.id
    try:
        await clbk.bot.delete_message(chat_id, previous_msg)
    except aiogram.exceptions.TelegramBadRequest:
        pass


def reset_csv(file_path = "data/admin_data.csv"):
    # Проверка существования файла
    if os.path.exists(file_path):
        os.remove(file_path)  # Удаление файла
        print(f"Файл {file_path} удален.")

    # Создание нового DataFrame с заданными столбцами
    df = pd.DataFrame(columns=['date', 'admin_msg'])

    # Сохранение DataFrame в новый CSV файл
    df.to_csv(file_path, index=False)
    print(f"Файл {file_path} создан с колонками: 'date' и 'admin_msg'.")