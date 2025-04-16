# API_Yatube

Учебный проект с REST API для социальной платформы, в которой пользователи могут публиковать посты, объединяться в группы и оставлять комментарии.

## 🚀 Описание

Этот проект — реализация backend-части блога в рамках учебной программы. Он построен с использованием Django и Django REST Framework. Реализована аутентификация через токены, поддерживаются CRUD-операции для постов и комментариев, а также работа с группами.

## 🛠 Технологии

- Python 3.10+
- Django 4.x
- Django REST Framework
- SQLite (по умолчанию)
- Postman (для тестирования)
- TokenAuthentication
- pytest (для тестов)

## 📦 Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/your-username/API_Yatube.git
   cd API_Yatube
   ```

2. Установите виртуальное окружение и зависимости:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Примените миграции и запустите сервер:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

4. (Опционально) Создайте суперпользователя:
   ```bash
   python manage.py createsuperuser
   ```

## 🔐 Аутентификация

Получение токена:
```http
POST /api/v1/api-token-auth/
Content-Type: application/json

{
  "username": "your_username",
  "password": "your_password"
}
```

Ответ:
```json
{
  "token": "your_token"
}
```

В дальнейшем токен передаётся в заголовке:
```
Authorization: Token your_token
```

## 📌 Эндпоинты

### Посты

- `GET /api/v1/posts/` — список всех постов
- `POST /api/v1/posts/` — создать пост
- `GET /api/v1/posts/{post_id}/` — получить пост
- `PUT/PATCH/DELETE /api/v1/posts/{post_id}/` — редактировать или удалить пост

Пример ответа на `GET /api/v1/posts/`:
```json
[
  {
    "id": 1,
    "text": "Мой первый пост!",
    "pub_date": "2025-04-16T12:34:56Z",
    "author": "testuser",
    "group": 1,
    "image": null
  }
]
```

### Комментарии

- `GET /api/v1/posts/{post_id}/comments/` — список комментариев к посту
- `POST /api/v1/posts/{post_id}/comments/` — добавить комментарий
- `GET /api/v1/posts/{post_id}/comments/{comment_id}/` — получить комментарий
- `PUT/PATCH/DELETE /api/v1/posts/{post_id}/comments/{comment_id}/` — редактировать или удалить комментарий

Пример ответа на `GET /api/v1/posts/1/comments/`:
```json
[
  {
    "id": 1,
    "author": "testuser",
    "post": 1,
    "text": "Отличный пост!",
    "created": "2025-04-16T13:45:00Z"
  }
]
```

### Группы

- `GET /api/v1/groups/` — список всех групп
- `GET /api/v1/groups/{group_id}/` — получить одну группу

## ✅ Покрытие тестами

Проект покрыт тестами. Используется стандартная библиотека тестирования Django и `pytest`.


## 📎 Дополнительно

- Можно использовать Postman для ручного тестирования запросов.
- Аутентифицированные пользователи могут создавать и редактировать свои посты и комментарии.
- Все изменения сохраняются в базе данных SQLite по умолчанию.

