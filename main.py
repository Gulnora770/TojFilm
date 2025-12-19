#!/usr/bin/env python
"""Утилита командной строки Django для административных задач."""
import os
import sys


def main():
    """Административные задачи."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tojfilm_site.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Не удалось импортировать Django. Убедитесь, что он установлен и доступен в вашей переменной окружения PYTHONPATH, и что вы активировали виртуальное окружение, если необходимо."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
