# django_1.6HW-03



Установим Django:
pip install django

запускаем приложение:
python manage.py runserver

Создан проект Django.
Добавлено в него 3 статические странички.
На одной из страниц контент повторяется 2 раза без изменения content (два раза прописано {{ flatpage.content }}).
Одна из страниц на сайте доступна только админу (только вошедшему пользователю).
На одной из страниц изменены шрифты и размеры текста.
Сайт представляет собой оформленный Bootstrap-шаблон со встроенными пользовательскими данными.
Статические файлы Bootstrap загружаются через теги {% load static %} и {% static %}
