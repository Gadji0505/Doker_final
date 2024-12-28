# Этап сборки
FROM python:3.9 AS builder
WORKDIR /app

# Копируем зависимости
COPY ./flask_app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем приложение
COPY ./flask_app/app.py .

# Этап выполнения
FROM python:3.9
WORKDIR /app

# Копируем установленные зависимости из предыдущего этапа
COPY --from=builder /app/app.py .

# Если у вас есть другие файлы, которые нужно скопировать, добавьте их здесь

CMD ["python", "app.py"]

