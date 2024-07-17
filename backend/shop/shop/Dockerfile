# Используем официальный образ Python в качестве базового образа
FROM python:3.9

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app
COPY . /app/

# Копируем файл requirements.txt внутрь контейнера
# COPY requirements.txt ./

# Устанавливаем зависимости, описанные в файле requirements.txt
RUN pip install -r requirements.txt
RUN mkdir -p /app/media
# Копируем проект внутрь контейнера

# Specify the command to run when the container starts
CMD python manage.py migrate \
    && python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='root').exists() or User.objects.create_superuser('root', 'root@example.com', 'root')" \
    && python manage.py collectstatic --no-input \
    && gunicorn shop.wsgi:application --bind 0.0.0.0:8080 --log-level info
