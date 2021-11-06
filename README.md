# Куда пойти — Москва глазами Артёма

Cайт о самых интересных местах в Москве.

![](static/mainpage.png)

## Ссылка на сайт
https://stanislavglazko.pythonanywhere.com/


## Аккаунт для тестирования сайта

- login: Irina
- password: irina_test_me


## Как запустить локально

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

## Как быстро добавить новое место на карте

1) Подготовить данные в JSON-формате, пример здесь:

https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%97%D0%B0%D0%B1%D1%80%D0%BE%D1%88%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9%20%D0%BF%D0%B8%D0%BE%D0%BD%D0%B5%D1%80%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BB%D0%B0%D0%B3%D0%B5%D1%80%D1%8C%20%C2%AB%D0%91%D0%B5%D0%BB%D0%BE%D0%B5%20%D0%BE%D0%B7%D0%B5%D1%80%D0%BE%C2%BB.json

2) В терминале набрать poetry run python manage.py load_place адрес_до_JSON_файла 

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

