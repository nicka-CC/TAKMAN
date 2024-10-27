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

# TODO: [backend] акаунт модера со статусом
# TODO: [backend] пополнение ски-пасса get, post, patch, delete
# TODO: [backend] покупка ски пасса get, patch, post, delete
# TODO: [backend] покупка сертификатов get, patch, post, delete
# TODO: [backend] трассы post, get, patch, delete
# TODO: [backend] бронирование коттеджей post, get, patch, delete
# TODO: [backend] бронировать коттеджи post, get, patch, delete
# TODO: [backend] коттеджи post, get, patch, delete
# TODO:[backend] афиша post, get, patch, delete
# TODO: [backend] наши услуги post, get, patch, delete
# TODO: [backend] бронировать инструмент post, get, patch, delete
# TODO:[backend] бронировать инструктура post, get, patch, delete


# TODO: [frontend] 1920 - 960 - mobile-first
# TODO:[frontend] pages (main, лыжи, проживание, услуги, цены, как добраться, ниформация, бронь инструктура, бронь инструмента, коттедж, events)
# TODO: [frontend] features(бронировать, бронировать инструмент, бронировать инструктура, пополнить, купить, купить билет)
# TODO: [frontend] entities(афиша, услуги, цены, качество, коттеджи, трассы)
# TODO: [frontend] widgets(хэдер, футэр, наши услуги. скипасс. на весь сезон, афиша, проживание, как добраться, контакты, трассы, коттедж, инструменты, услуги, прайс на проживание, туры)
# TODO: [frontend] shared(кнопка(обычная, прозрачная), инпут)