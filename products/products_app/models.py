from django.db import models
from django.core.validators import MinValueValidator

category_choices = (
    ('other', 'разное'),
    ('phone', 'телефон'),
    ('notebook', 'ноутбук')
)


class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    text = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    category = models.CharField(max_length=150, choices=category_choices, default='other', verbose_name='Категория')
    remainder = models.IntegerField(validators=[MinValueValidator(0)], verbose_name='Остаток')
    cost = models.DecimalField(max_digits=9, decimal_places=2, validators=[MinValueValidator(0)], verbose_name='Стоимость')

    class Meta:
        db_table = 'products'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.id}. {self.name}: {self.text}'
