# Generated by Django 3.2 on 2022-11-16 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_applicant_resume_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='category',
            field=models.TextField(blank=True, choices=[('IT', 'IT'), ('Management', 'Менеджмент'), ('Audit', 'Аудит'), ('HR', 'HR')], null=True, verbose_name='Категория вакансии'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='salary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Желаемая зарплата'),
        ),
    ]