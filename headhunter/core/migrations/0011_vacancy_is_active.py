# Generated by Django 3.2 on 2022-11-20 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_vacancy_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Скрыть вакансию'),
        ),
    ]
