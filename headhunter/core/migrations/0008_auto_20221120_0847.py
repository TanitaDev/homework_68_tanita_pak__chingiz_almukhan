# Generated by Django 3.2 on 2022-11-20 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_vacancy_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Последние изменение'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления'),
        ),
    ]