# Куда пойти — Москва глазами Артёма

Cайт о самых интересных местах в Москве.

![](static/mainpage.png)

## Ссылка на сайт
https://stanislavglazko.pythonanywhere.com/


## Как запустить

1) Установите Python
2) Установите Poetry: 
https://python-poetry.org/docs/#installation

3) Склонируйте репозиторий
4) Перейдите в папку с проектом
5) Установите зависимости:
    ```
    poetry install 
    ```
6) Примените миграции 
    ```
    poetry run python manage.py migrate
    ```
7) Запустите проект 
    ```
    poetry run python manage.py runserver
    ```

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 2 переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта

## Используемые библиотеки

* [Leaflet](https://leafletjs.com/) — отрисовка карты
* [loglevel](https://www.npmjs.com/package/loglevel) для логгирования
* [Bootstrap](https://getbootstrap.com/) — CSS библиотека
* [Vue.js](https://ru.vuejs.org/) — реактивные шаблоны на фронтенде

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).

