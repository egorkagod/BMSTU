from datetime import datetime
import os

from django.views import View
from django.http import HttpRequest, JsonResponse

from django.conf import settings


def sync_users(request):
    with open(os.path.join(settings.BASE_DIR, 'sync_users.json'), 'a+') as f:
        f.write('%s\n%s\n\n' % (datetime.now(), request.body.decode(), ))
    return JsonResponse({'success': True})

def sync_orders(request):
    with open(os.path.join(settings.BASE_DIR, 'sync_orders.json'), 'a+') as f:
        f.write('%s\n%s\n\n' % (datetime.now(), request.body.decode(), ))
    return JsonResponse({'success': True})

def sync_ready_orders(request):
    with open(os.path.join(settings.BASE_DIR, 'sync_ready_orders.json'), 'a+') as f:
        f.write('%s\n%s\n\n' % (datetime.now(), request.body.decode(), ))
    return JsonResponse({'success': True})