import asyncio

from django.conf import settings
from django.core.management.base import BaseCommand

from telegram import Bot


async def logOut():
    bot = Bot(token=settings.BOT_TOKEN)
    result = await bot.log_out()
    return result

class Command(BaseCommand):
    def handle(self, *args, **options):
        result = asyncio.run(logOut())
        self.stdout.write(self.style.SUCCESS(f"Logout result: {result}"))
