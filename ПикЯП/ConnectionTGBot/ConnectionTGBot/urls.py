from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from bot import api_views
from bot.views import TelegramBotWebhookView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('telegram/', csrf_exempt(TelegramBotWebhookView.as_view())),
    path('api/users/', csrf_exempt(api_views.sync_users)),
    path('api/orders/', csrf_exempt(api_views.sync_orders)),
    path('api/ready-orders/', csrf_exempt(api_views.sync_ready_orders)),
]
