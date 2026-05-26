# chat_avito
Чат для авито, который способен отвечать на сообщения и выдавать ответы на основе загруженных данных (по типу примерные работы и стоимость работы)

# Avito AI Bot

AI-бот для автоматизации общения с клиентами на Avito в сфере остекления.

Проект разрабатывается как модульная система с возможностью постепенного перехода:

```text
Browser Automation (Playwright)
↓
Unified Messenger Adapter
↓
Dialog Manager
↓
Knowledge Retrieval
↓
LLM
↓
Response Formatter
↓
Messenger Adapter
```

На текущем этапе используется browser automation через Playwright.
Архитектура изначально проектируется таким образом, чтобы в будущем можно было перейти на Avito API без переписывания основной логики.

---

# Цели проекта

## MVP

На первом этапе бот должен:

* читать новые сообщения на Avito;
* автоматически отвечать на базовые вопросы;
* задавать уточняющие вопросы;
* использовать базу знаний;
* выдавать примерные диапазоны цен;
* передавать сложные диалоги человеку;
* сохранять историю сообщений.

---

# Основные принципы проекта

## 1. Независимость от транспорта

Playwright не должен содержать бизнес-логику.

Browser automation — только транспортный слой.

Вся логика:

* AI;
* хранение данных;
* управление диалогом;
* retrieval;
* форматирование ответа;

должна быть независимой от конкретного источника сообщений.

---

## 2. Возможность перехода на Avito API

В будущем предполагается переход:

```text
PlaywrightAdapter → AvitoApiAdapter
```

без изменения:

* AI;
* retrieval;
* database layer;
* dialog manager.

---

## 3. Минимизация расходов

Проект ориентирован на:

* локальный запуск;
* локальные LLM;
* минимальные ежемесячные расходы;
* отсутствие облачной инфраструктуры.

---

# Технологический стек

## Backend

* Python
* FastAPI

## Browser Automation

* Playwright

## Database

* PostgreSQL

## AI

* Ollama
* Qwen / Gemma / другие локальные модели

## Infrastructure

* Docker
* Docker Compose

## Version Control

* Git
* GitHub

---

# Планируемая структура проекта

```text
avito-ai-bot/
│
├── app/
│   ├── ai/
│   ├── api/
│   ├── bot/
│   ├── core/
│   ├── db/
│   ├── messenger/
│   │   ├── base.py
│   │   ├── avito_browser/
│   │   └── avito_api/
│   ├── retrieval/
│   └── services/
│
├── data/
│   ├── faq/
│   ├── prices/
│   ├── prompts/
│   └── works/
│
├── docker/
├── docs/
│   ├── architecture/
│   ├── decisions/
│   ├── progress/
│   └── research/
│
├── tests/
│
├── .env.example
├── .gitignore
├── docker-compose.yml
├── README.md
└── requirements.txt
```

---

# Архитектурные принципы

## Adapter Pattern

Каждый источник сообщений реализует единый интерфейс:

```python
class MessengerAdapter:
    async def get_new_messages(self):
        pass

    async def send_message(self, chat_id: str, text: str):
        pass
```

Это позволит:

* заменить browser automation на API;
* подключить Telegram;
* подключить WhatsApp;
* подключить веб-чат;
* тестировать систему независимо от транспорта.

---

# Структура данных

## Normalized Incoming Message

```python
class IncomingMessage:
    chat_id: str
    user_id: str
    text: str
    timestamp: datetime
    attachments: list
```

Все источники сообщений должны приводиться к единому формату.

---

# План развития проекта

## Этап 1 — MVP

* Playwright
* чтение сообщений
* отправка сообщений
* PostgreSQL
* базовые автоответы
* сохранение диалогов

---

## Этап 2 — AI Layer

* Ollama
* локальная LLM
* генерация ответов
* prompt templates

---

## Этап 3 — Retrieval System

* FAQ
* прайсы
* примеры работ
* поиск релевантной информации

---

## Этап 4 — Dialog Management

* состояние диалога
* классификация intent
* lead scoring
* escalation logic

---

## Этап 5 — Vision

* анализ фотографий
* определение типа окна
* распознавание проблем

---

# Правила работы с Git

## В репозиторий НЕ загружаются

* .env
* cookies
* session storage
* токены
* реальные базы данных
* пользовательские данные
* большие модели
* временные файлы
* логи

---

# Пример .gitignore

```gitignore
.env
*.db
__pycache__/
playwright_storage/
models/
logs/
data/private/
*.log
```

---

# Environment Variables

Пример:

```env
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=

OLLAMA_URL=
MODEL_NAME=

AVITO_LOGIN=
AVITO_PASSWORD=
```

---

# Документация проекта

## docs/architecture/

Описание архитектуры системы.

---

## docs/decisions/

Архитектурные решения:

* почему выбран Playwright;
* почему PostgreSQL;
* стратегия миграции на API;
* ограничения browser automation.

---

## docs/progress/

Журнал прогресса разработки.

Формат:

```text
YYYY-MM-DD.md
```

Содержимое:

* что сделано;
* проблемы;
* найденные решения;
* дальнейшие задачи.

---

# Текущий статус

## Текущий этап

Подготовка архитектуры и инфраструктуры проекта.

---

## Ближайшие задачи

1. Создать базовую структуру проекта
2. Настроить Docker Compose
3. Подключить PostgreSQL
4. Поднять Playwright
5. Реализовать получение сообщений
6. Реализовать отправку сообщений
7. Реализовать базовый Messenger Adapter

---

# Важные замечания

## Browser Automation

На текущем этапе проект использует browser automation.

Это временное архитектурное решение, обусловленное:

* отсутствием бизнес-аккаунта;
* ограничениями Avito API;
* необходимостью быстрого MVP.

Проект изначально разрабатывается с учётом возможной миграции на официальный API.

---

# License

Проект разрабатывается в образовательных и исследовательских целях.
