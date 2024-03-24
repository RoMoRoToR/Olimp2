# Используем официальный образ Python как базовый
FROM python:3.8-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app

# Устанавливаем зависимости
RUN pip install Flask

# Задаем переменную среды для Flask
ENV FLASK_APP=main.py

# Запускаем приложение Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=9025"]
