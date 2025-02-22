🏪 Cafe Order System


📌 Описание

Cafe Order System – это система управления заказами в кафе, разработанная на Django с поддержкой PostgreSQL.
Она позволяет добавлять, редактировать, удалять и фильтровать заказы, а также рассчитывать общую выручку.

🚀 Функции

Добавление и редактирование заказов – через удобный веб-интерфейс без необходимости вводить JSON.
Фильтрация заказов по статусу – возможность быстро найти заказы в нужном состоянии.
Удаление заказов с подтверждением – всплывающее окно перед удалением заказа.
Отображение общей выручки – через всплывающее модальное окно.
Обновленный интерфейс – улучшенная стилизация без сторонних CSS-фреймворков.
Поддержка PostgreSQL – все данные хранятся в надежной СУБД.
Обработка ошибок – более детальная валидация и сообщения пользователю.
Тестирование – написаны автоматические тесты (unittest/Pytest).
Документация – добавлены аннотации к функциям, README и техническое описание.

🛠 Технологии

Python 3
Django
PostgreSQL
HTML, CSS, Bootstrap (только для стилизации), чистый JavaScript (для интерактивности)

📦 Установка и запуск

1. Клонировать репозиторий:
    git clone https://github.com/ArT-191/Cafe_Order_System.git
    cd Cafe_Order_System

2. Создать и активировать виртуальное окружение:
    python -m venv venv
    source venv/bin/activate  # MacOS/Linux
    venv\Scripts\activate     # Windows

3. Установить зависимости:
    pip install -r requirements.txt

4. Настроить базу данных:
    Указать параметры PostgreSQL в settings.py
    Применить миграции:
    python manage.py migrate
    
5. Запустить сервер:
    python manage.py runserver
    

✅ Тестирование

Запуск тестов выполняется командой:
    pytest  # Если использован Pytest
    python manage.py test  # Если unittest
    
📄 Лицензия

Проект распространяется под лицензией MIT.



    
