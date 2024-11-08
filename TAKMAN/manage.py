#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TAKMAN.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


# TODO: [frontend] 1920 - 960 - mobile-first
# TODO:[frontend] pages (услуги, цены, как добраться, ниформация, бронь инструктура, бронь инструмента, коттедж, events)
# TODO: [frontend] features (бронировать инструмент, бронировать инструктура, купить билет)
# TODO: [frontend] entities (цены, качество)
# TODO: [frontend] widgets (инструменты, прайс на проживание, туры)