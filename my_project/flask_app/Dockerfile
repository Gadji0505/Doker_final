# Этап сборки
FROM python:3.9-slim AS builder

WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt ./
# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Этап финального образа
FROM python:3.9-slim

WORKDIR /app

# Копируем установленные зависимости из этапа сборки
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /app /app

# Копируем остальной код приложения
COPY . .

# Указываем команду для запуска приложения
CMD ["python", "app.py"]
