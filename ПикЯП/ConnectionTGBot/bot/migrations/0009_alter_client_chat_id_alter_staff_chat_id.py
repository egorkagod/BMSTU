# Generated by Django 5.1.4 on 2024-12-09 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0008_client_active_client_uid_order_uid_staff_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='chat_id',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='staff',
            name='chat_id',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
