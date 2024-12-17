from django.conf import settings
from telegram.ext import Application


application = Application \
                    .builder() \
                    .base_url(settings.BOT_BASE_URL) \
                    .token(settings.BOT_TOKEN) \
                    .build()