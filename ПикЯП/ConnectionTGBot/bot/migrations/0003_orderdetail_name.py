# Generated by Django 5.1.3 on 2024-11-17 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_orderdetail_is_accepted_alter_order_staff_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
