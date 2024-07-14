from django.core.validators import MinValueValidator
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    """"
    Модель продукта
    """
    name = models.CharField(max_length=100, verbose_name='Название')
    model = models.CharField(max_length=100, verbose_name='Модель')
    date = models.DateField(verbose_name='Дата выхода продукта на рынок')
    seller = models.ForeignKey('Seller', on_delete=models.CASCADE, verbose_name='Продавец')

    def __str__(self):
        return f'{self.name} {self.model} {self.date}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Contact(models.Model):
    """"
    Модель контакта
    """
    email = models.EmailField(max_length=254, verbose_name='E-mail')
    country = models.CharField(max_length=100, verbose_name='Страна', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)
    street = models.CharField(max_length=100, verbose_name='Улица', **NULLABLE)
    house_number = models.PositiveIntegerField(verbose_name='Номер дома', **NULLABLE)
    seller = models.ForeignKey('Seller', on_delete=models.CASCADE, related_name='seller_contact',
                               verbose_name='Продавец')

    def __str__(self):
        return f'{self.email} ({self.city if self.city else ''}, ул. {self.street if self.street else ''}, \
{self.house_number if self.house_number else ''})'

    def save(self, *args, **kwargs):
        self.city = self.city.title()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Seller(models.Model):
    """"
    Модель звена торговой сети
    """
    SELLER_CHOICES = [
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель')
    ]
    seller_type = models.PositiveSmallIntegerField(choices=SELLER_CHOICES, verbose_name='Продавец')
    name = models.CharField(max_length=100, verbose_name='Название')
    provider = models.ForeignKey('Seller', on_delete=models.PROTECT, verbose_name='Поставщик', **NULLABLE)
    level = models.PositiveSmallIntegerField(verbose_name='Уровень')
    debt = models.DecimalField(verbose_name='Задолженность перед поставщиком', max_digits=12, decimal_places=2,
                               validators=[MinValueValidator(0)], **NULLABLE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')

    def __str__(self):
        return f'{self.seller_type} {self.name}'

    class Meta:
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'
