# Используем официальный образ Python как базовый
FROM python:3.12

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app

# Устанавливаем зависимости
RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 9025

ENV FLASK_APP=main.py

# Запускаем приложение Flask
CMD ["python", "main.py"]