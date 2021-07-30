from django.db import models
from utils.models import generate_unique_slug


class Brand(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=210, default='', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_unique_slug(Brand, self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Бренды'
        verbose_name = 'Бренд'


class Option(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Опции'
        verbose_name = 'Опция'


class Auto(models.Model):
    AUTO_CLASS_ECONOMY = 'e'
    AUTO_CLASS_COMFORT = 'c'
    AUTO_CLASS_BUSINESS = 'b'

    AUTO_CLASS_CHOICES = [
        (AUTO_CLASS_ECONOMY, 'economy'),
        (AUTO_CLASS_COMFORT, 'comfort'),
        (AUTO_CLASS_BUSINESS, 'business'),
    ]

    brand = models.ForeignKey(Brand, null=True, on_delete=models.CASCADE, related_name='cars', verbose_name='Бренд')
    options = models.ManyToManyField(Option, related_name='cars', verbose_name='Опции')
    number = models.CharField(max_length=15, verbose_name='Номер')
    description = models.TextField(max_length=500, default='', blank=True, verbose_name='Описание')
    year = models.PositiveSmallIntegerField(null=True, verbose_name='Год')
    auto_class = models.CharField(max_length=1, null=True, choices=AUTO_CLASS_CHOICES,
                                  default=AUTO_CLASS_ECONOMY, verbose_name='Класс авто')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name_plural = 'Автомобили'
        verbose_name = 'Автомобиль'


class VehiclePassport(models.Model):
    auto = models.OneToOneField(Auto, on_delete=models.CASCADE, related_name='pts')
    vin = models.CharField(max_length=30, verbose_name='Идентификационный номер (VIN)')
    engine_volume = models.PositiveSmallIntegerField(verbose_name='Объем двигателя, куб.см')
    engine_power = models.PositiveSmallIntegerField(verbose_name='Мощность двигателя, л.с.')

    def __str__(self):
        return f'{self.auto}::{self.vin}'

    class Meta:
        verbose_name_plural = 'Паспорта машин'
        verbose_name = 'Пастпорт машины'
