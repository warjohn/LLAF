import csv

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class Storage:
    """main storage class for all data"""

    def __init__(self):
        pass

    @classmethod
    def __init_table(cls, table_name, sheet_name):
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "data/llaf-438714-aea04f5c8255.json", scope)
        client = gspread.authorize(creds)
        print("client", client)
        spreadsheet = client.open(table_name)
        print("spreadsheet", spreadsheet)
        selected_sheet = spreadsheet.worksheet(sheet_name)
        return selected_sheet  # Возвращаем объект листа gspread

    @classmethod
    def add_data(cls, table_name, sheet_name, user_id, nickname, user_text, model_response):
        sheet = cls.__init_table(table_name, sheet_name)
        
        # Получаем все значения из листа gspread
        values = sheet.get_all_values()  
        
        # Находим первую пустую строку, начиная с 2-й (пропуская заголовки)
        row_to_insert = len(values) + 1  # Изначально предполагаем, что добавим в конец

        # Проверяем строки начиная со 2-й, чтобы найти первую пустую строку
        for i in range(1, len(values)):
            if not any(values[i]):  # Если вся строка пустая
                row_to_insert = i + 1  # Устанавливаем строку для вставки
                break

        # Записываем данные в ячейки
        sheet.update(f'A{row_to_insert}', [[user_id, nickname, user_text, model_response]])  # Заполняем данные

    @classmethod
    def get_button_text(cls, table_name, sheet_name, storage):
        sheet = cls.__init_table(table_name, sheet_name)
        values = sheet.get_all_values()
        df = pd.DataFrame(values)

        # Инициализируем списки
        start_button_text = []
        aboutUS_button_text = []
        wannaBUY_button_text = []
        goodsExpert_button_text = []

        # Заполняем списки данными из соответствующих столбцов
        for index, row in df.iloc[1:].iterrows():
            start_button_text.append(row[0])
            aboutUS_button_text.append(row[1])
            wannaBUY_button_text.append(row[2])
            goodsExpert_button_text.append(row[3])

        storage.set_columns(start_button_text, aboutUS_button_text, wannaBUY_button_text, goodsExpert_button_text)


    @classmethod
    def get_texts(cls, table_name, sheet_name, storage):
        sheet = cls.__init_table(table_name, sheet_name)
        value = sheet.get_all_values()
        df = pd.DataFrame(value)

        # Предположим, что нужные столбцы имеют индексы 0, 1, и 2 (первые три)
        col1_values = df.iloc[1:, 0].tolist()  # Значения из первого столбца
        col2_values = df.iloc[1:, 1].tolist()  # Значения из второго столбца
        col3_values = df.iloc[1:, 2].tolist()  # Значения из третьего столбца

        print(col1_values, col2_values, col3_values, sep = '\n')
        storage.set_texts(col1_values, col2_values, col3_values)

