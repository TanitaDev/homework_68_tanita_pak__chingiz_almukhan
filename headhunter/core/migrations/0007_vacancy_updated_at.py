# Generated by Django 3.2 on 2022-11-19 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20221119_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='Дата обновления'),
        ),
    ]
