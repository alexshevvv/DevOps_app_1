# Используем официальный образ Python в качестве базового
FROM python:3.9-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта в рабочую директорию контейнера
COPY . /app

# Команда, которая будет запущена при старте контейнера
CMD ["python", "calc_app.py"]
