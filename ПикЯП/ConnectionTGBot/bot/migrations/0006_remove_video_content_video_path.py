# Generated by Django 5.1.3 on 2024-11-17 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0005_video_data_seen_video_data_sent_alter_video_comment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='content',
        ),
        migrations.AddField(
            model_name='video',
            name='path',
            field=models.FileField(default='e', upload_to=''),
        ),
    ]
