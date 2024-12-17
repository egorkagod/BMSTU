from django.contrib import admin

from bot import models


@admin.register(models.Staff)
class StaffAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    pass