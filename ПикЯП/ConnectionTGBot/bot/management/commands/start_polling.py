from django.core.management.base import BaseCommand
from bot.main import application


class Command(BaseCommand):
    help = 'Начало прослушивания сообщений боту'

    def handle(self, *args, **options):
        application.run_polling()