from django.db import models
from django.utils import timezone

tz = timezone.get_default_timezone()


class Worker(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    phone_number = models.CharField(max_length=255, verbose_name='Номер телефона')

    def __str__(self):
        return self.name


class Store(models.Model):
    title = models.CharField(max_length=100, verbose_name='Торговая точка')
    worker = models.ForeignKey(
        'Worker',
        default=None,
        null=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title


class Visit(models.Model):
    visited_at = models.DateTimeField(verbose_name='Дата посещения', auto_now_add=True)
    store = models.ForeignKey(
        'Store',
        default=None,
        null=True,
        on_delete=models.CASCADE
    )
    latitude = models.FloatField(verbose_name='Широта')
    longtitude = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return f'{self.store.title} {format(self.visited_at.astimezone(tz).strftime("%d-%m-%Y %H:%M"))}'
