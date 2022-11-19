# Generated by Django 3.2 on 2022-11-19 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_vacancy_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='author',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='vacancy', to=settings.AUTH_USER_MODEL, verbose_name='Автор вакансии'),
        ),
    ]
