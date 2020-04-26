# Generated by Django 3.0.5 on 2020-04-26 07:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sub_persones', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classes', '0002_auto_20200426_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sub_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sub_persones.SubPerson')),
            ],
        ),
        migrations.AlterField(
            model_name='image',
            name='belongs_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='classes.TheClass'),
        ),
        migrations.AlterField(
            model_name='theclass',
            name='main_person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='the_class', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='video',
            name='belongs_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='classes.TheClass'),
        ),
        migrations.DeleteModel(
            name='Opinions',
        ),
        migrations.AddField(
            model_name='opinion',
            name='the_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opiniones', to='classes.TheClass'),
        ),
    ]
