import json
import os
from django.views import View
from django.http import HttpRequest, JsonResponse

from django.conf import settings

from telegram import Update
from .main import application


class TelegramBotWebhookView(View):
    async def post(self, request: HttpRequest) -> JsonResponse:
        with open(os.path.join(settings.BASE_DIR, 'telegram.log'), 'a+') as f:
            f.write(request.body.decode() + '\n\n')
        update = Update.de_json(data=json.loads(request.body), bot=application.bot)
        application.update_queue.put_nowait(update)
        return JsonResponse({'ok': True})

    async def get(self, request: HttpRequest) -> JsonResponse:
        return JsonResponse({'ok': 'Get requests are not supported!'})