# Generated by Django 3.0.5 on 2020-04-23 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_auto_20200423_1144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theclass',
            name='available',
        ),
        migrations.RemoveField(
            model_name='theclass',
            name='is_done',
        ),
        migrations.RemoveField(
            model_name='theclass',
            name='main_person',
        ),
        migrations.RemoveField(
            model_name='theclass',
            name='start_at',
        ),
        migrations.RemoveField(
            model_name='theclass',
            name='video_file',
        ),
    ]
