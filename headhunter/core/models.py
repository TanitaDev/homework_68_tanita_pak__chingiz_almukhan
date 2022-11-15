
from django.db import models

from accounts.models import Profile

CATEGORY = (('IT', 'IT'), ('Management', 'Менеджмент'), ('Audit', 'Аудит'), ('HR', 'HR'))


class Resume(models.Model):
    category = models.TextField(verbose_name='Категория вакансии', choices=CATEGORY, null=False, blank=False)
    about = models.TextField(max_length=500, verbose_name='О себе')
    salary = models.DecimalField(verbose_name='Желаемая зарплата')
    applicant = models.ForeignKey(Profile, verbose_name='Соискатель', on_delete=models.CASCADE)
    updated_at = models.DateField(verbose_name='Последние изменение', auto_now=True)
    is_active = models.BooleanField(verbose_name='Скрыть резюме', default=False, null=False)
    telegram = models.CharField(verbose_name='Ссылка на телеграм', max_length=100, null=True, blank=True)
    linkedin = models.CharField(verbose_name='Ссылка на Linkedin', max_length=100, null=True, blank=True)
    facebook = models.CharField(verbose_name='Ссылка на Facebook', max_length=100, null=True, blank=True)

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()


class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    study = models.CharField(max_length=100, verbose_name='Место обучения')
    start_date = models.DateField(blank=True, null=True, verbose_name='Начал обучаться')
    end_date = models.DateField(blank=True, null=True, verbose_name='Закончил обучаться')


class Job(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, verbose_name='Обязанности')
    company = models.CharField(max_length=100, verbose_name='Название компании')
    start_date = models.DateField(blank=True, null=True, verbose_name='Начал работать')
    end_date = models.DateField(blank=True, null=True, verbose_name='Закончил работать')
