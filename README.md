# 🛒 OnlineShop Production

**OnlineShop Production** — это серверная часть телеграм-магазина, разработанная на **Django REST Framework**, с полной интеграцией через **Telegram Web App**. Система обеспечивает управление товарами, приём заказов и административный контроль через админку Django.


---

## 📲 Telegram WebApp (Frontend)

Этот backend обслуживает клиент, написанный специально для Telegram:


---

## 🚀 Основной функционал

- 📦 Просмотр каталога товаров
- 🛍️ Оформление и обработка заказов через Telegram
- ⚙️ REST API для Telegram WebApp
- 🧑‍💼 Django админ-панель для управления товарами и заказами
- 🐳 Возможность развёртывания через Docker

---

## 🛠️ Технологии

| Технология         | Назначение                                    |
|--------------------|-----------------------------------------------|
| Python 3.x         | Язык программирования                         |
| Django             | Веб-фреймворк                                 |
| Django REST        | Создание REST API                             |
| PostgreSQL         | База данных                                   |
| Telegram Web App   | Взаимодействие с пользователем через Telegram |
| Docker             | Контейнеризация и удобный деплой              |

---


---

## ⚙️ Установка (локально)

1. **Клонировать репозиторий:**
  
 - git clone https://github.com/DELTA-0924/onlineshop_production.git
 - cd onlineshop_production

2.**Создать и активировать виртуальное окружение**:



  - python -m venv venv
  - source venv/bin/activate   # Windows: venv\Scripts\activate

3.**Установить зависимости:**


 - pip install -r requirements.txt

4.**Применить миграции и создать суперпользователя:**

  - python manage.py migrate
  - python manage.py createsuperuser

5. **Запустить сервер:**


  - python manage.py runserver

## 🐳 Развёртывание через Docker

**Если у вас установлен Docker и Docker Compose, вы можете быстро запустить проект в контейнере:**

6. **Собрать и запустить контейнеры:**

  - docker-compose up --build
