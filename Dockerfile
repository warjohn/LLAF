# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /LLAF

# Скопировать файл requirements.txt в рабочую директорию
COPY requirements.txt .

# Установить зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Скопировать все файлы в рабочую директорию контейнера
COPY . .

# Команда для запуска бота
CMD ["python", "main.py"]
