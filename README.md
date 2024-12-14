# Task Management System

## Описание
Данная система позволяет управлять задачами, пользователями и проектами. Задачи могут быть назначены пользователям и проектам, а также проверяться на просроченность.

## Основной функционал
- Создание задач.
- Назначение задач пользователям и проектам.
- Удаление задач.
- Проверка просроченных задач.

## Изменения и улучшения
- Произведен рефакторинг кода для улучшения читаемости и структуры.
- Добавлены комментарии к ключевым методам.
- Исправлены значения статусов задач: теперь используются "New" и "Deleted" для единообразия.
- Улучшена типизация, добавлены аннотации типов для всех классов и методов.
- Оптимизирован метод `is_overdue` для проверки просроченности задач.
- Подготовлен базовый юнит-тест для создания задач. Рекомендации даны для написания дополнительных тестов.

## Запуск
1. Запустите тесты:
   ```bash
   python -m unittest test_task_manager.py
   ```
