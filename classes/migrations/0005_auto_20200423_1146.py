# Generated by Django 3.0.5 on 2020-04-23 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_auto_20200423_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='theclass',
            name='available',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='theclass',
            name='start_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='theclass',
            name='is_done',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
