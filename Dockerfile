# Используем официальный образ Python
FROM python:3.9

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл зависимостей в рабочую директорию
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы в рабочую директорию
COPY . .

# Указываем команду запуска контейнера
CMD ["python", "flask_calc_app.py"]
