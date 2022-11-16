from django.db import models


class Vacancy(models.Model):
    IT = 'IT'
    DES = 'DESIGN'
    MAN = 'MANAGEMENT'
    MED = 'MEDICINE'
    ENG = 'ENGINEERING'
    ART = 'ART'
    TRS = 'TRANSPORT'
    MRK = 'MARKETING'
    TRD = 'TRADE'
    ECN = 'ECONOMY'
    CATEGORY_CHOICES = [
        (IT, 'IT'),
        (DES, 'Дизайн'),
        (MAN, 'Менеджмент'),
        (MED, 'Медицина'),
        (ENG, 'Инженерное дело'),
        (ART, 'Искусство'),
        (TRS, 'Транспорт'),
        (MRK, 'Маркетинг'),
        (TRD, 'Торговля'),
        (ECN, 'Экономика')
    ]

    name = models.CharField(max_length=200, verbose_name='Название вакансии', null=False, blank=False)
    salary = models.DecimalField(verbose_name='Заработная плата', decimal_places=1, max_digits=10, null=False, blank=False)
    description = models.TextField(max_length=3000, verbose_name='Описание вакансии', null=False, blank=False)
    experience = models.FloatField(verbose_name='Опыт работы', null=False, blank=False)
    category = models.TextField(verbose_name='Категория вакансии', null=False, blank=False, choices=CATEGORY_CHOICES,
                                default=IT)
