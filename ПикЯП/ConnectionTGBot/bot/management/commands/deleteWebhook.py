import asyncio

from django.conf import settings
from django.core.management.base import BaseCommand

from telegram import Bot


async def deleteWebhook():
    bot = Bot(token=settings.BOT_TOKEN)
    result = await bot.deleteWebhook()
    return result

class Command(BaseCommand):
    def handle(self, *args, **options):
        result = asyncio.run(deleteWebhook())
        self.stdout.write(self.style.SUCCESS(f'setWebhook result: {result}'))
