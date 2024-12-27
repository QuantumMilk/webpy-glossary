# webpy-glossary
Создание базы для реализации производственной практики, а также выполнения задания по дисциплине "Проектирование и развертывание веб-решений в эко-системе Python"

***

Одна из реализаций WebAPI для глоассария с использованием FastAPI, Docker и SQLite.

# API Endpoints 

1. Получение всех терминов

`GET /terms`

Ответ:
```
[
  {
    "id": 1,
    "term": "API",
    "description": "Application Programming Interface"
  }
]
```

2. Получение термина по ключевому слову

`GET /terms/{term}`

3. Добавление нового термина

`POST /terms`

Тело запроса:
```
{
  "term": "API",
  "description": "Application Programming Interface"
}
```

4. Обновление существующего термина

`PUT /terms/{term}`

Тело запроса:
```
{
  "description": "Updated description"
}
```

5. Удаление термина

`DELETE /terms/{term}`

# Развернуть контейнер локально

Для начала выполните `docker pull quantummilk/glossary-api`

Затем запустите контейнер `docker run -d --name <CONTAINER_NAME> -p 80:8000 glossary-api`

Для проверки запуска контейнера используйте `docker ps`

Чтобы контейнер запускался при перезагрузке сервера: 
```
docker update --restart always <CONTAINER_NAME>
```