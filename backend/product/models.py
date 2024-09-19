from django.core.validators import MinValueValidator
from django.db import models

from backend.constants import MAX_NAME_LENGTH, MIN_PRICE


class Product(models.Model):
    """
    Модель для продуктов.
    """
    name = models.CharField('Название', max_length=MAX_NAME_LENGTH)
    description = models.TextField('Описание')
    price = models.FloatField('Цена', validators=[MinValueValidator(MIN_PRICE)])

    class Meta:
        ordering = ('name', )
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name
