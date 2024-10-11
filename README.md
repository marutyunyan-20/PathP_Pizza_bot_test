# Telegram бота на Aiogram 3 + SQLAlchemy

Данный проект представляет собой практическое применине знаний по  **Aiogram 3**, **SQLAlchemy**, для создания тг  бота для пиццерии.

####  Стек

- **Telegram API**: Aiogram 3
- **ORM**: SQLAlchemy с aiosqlite
- **База данных**: [PostgreSQL](https://www.postgresql.org/)


### Структура проекта

```
├─ app
│  ├─ common
│  │  ├─ bot_cmds_list.py
│  │  ├─ restricted_words.py
│  │  ├─ texts_for_db.py
│  │ 
│  ├─ database
│  │  ├─ engine.py
│  │  ├─ models.py
│  │  ├─ orm_query.py
│  │  
│  ├─ filters
│  │  ├─ chat_types.py
│  │ 
│  ├─ handlers
│  │  ├─ admin_private.py
│  │  ├─ menu_processing.py
│  │  ├─ user_group.py
│  │  ├─ user_private.py
│  │ 
│  ├─ keyboards
│  │  ├─ inline.py
│  │  ├─ reply.py
│  │
│  ├─ middlewares
│  │  ├─ db.py
│  │ 
│  └─ utils
│     ├─ paginator.py
│
├─ manage.py
└─ requirements.txt

```
### Переменные окружения

Создайте файл `.env` в корне проекта:

```env
BOT_TOKEN=your_bot_token_here
DB_URL=postgresql+asyncpg://login:password@localhost:5432/db_name - подключение к БД Postgresql
DB_LITE=sqlite+aiosqlite:///my_base.db - - подключение к БД Sqlite3
```

- `BOT_TOKEN`: Получите у [BotFather](https://t.me/BotFather)
- `DB_URL`: Через SQL Shell или pgAdmin 4 создаете БД, и заменяете login и password на логин и пароль, созданового вами админа для вашей бд, db_name заменяете на имя вашей БД.
- **Пример**:DB_URL=postgresql+asyncpg://bot:bot@localhost:5432/bot

Старая схема БД не подойдет для этого бота, поэтому при запуске этого бота в !первый раз - удалить старые таблицы (это уже предусмотрено, нужно раскоментировать на !первый запуск эту строчку кода в файле app.py:

```
  async def on_startup(bot):
  эту
  # await drop_db()  <------ЭТУ

    await create_db()
```

Для получения админки следует создать группу, добавить в нее бота, присвоить ему статус администратора и прописать комануду "/admin" в чат, после чего он ее удалит и можно будет настраивать бота под себя.

!!!!
Бот не запуститься после команды "/start", пока не будут добавлены банеры через админку
!!!

### Зависимости

```
aiogram
python-dotenv
sqlalchemy
asyncpg
aiosqlite

```

## Начало работы

1. Клонируйте репозиторий:
```bash
git clone https://github.com/marutyunyan-20/PathP_Pizza_bot_test.git.
```

2.Создайте и активируйте свою виртуальную среду:
```bash
python -m venv .venv
```
Windows:
```powershell
.venv/Scripts/activate
```
Linux и MacOS-systems:
```bash
source .venv/bin/activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Запустите бота:
Windows:
```bash
python manage.py 
```
Linux и MacOS-systems:
```bash
python3 manage.py 
```
