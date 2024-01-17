from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    title = models.CharField(max_length=250, verbose_name='название продукта')
    description = models.TextField(verbose_name='описание продукта')
    image = models.ImageField(upload_to='products_images/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, **NULLABLE, verbose_name='категория продукта')
    price = models.IntegerField(verbose_name='цена за 1шт. товара')
    date_of_creation = models.DateField()
    date_of_change = models.DateField()

    def __str__(self):
        return f'{self.title} {self.price}'


class Category(models.Model):
    title = models.CharField(max_length=250, verbose_name='название категории')
    description = models.TextField(verbose_name='описание категории')
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, **NULLABLE, verbose_name='вышестоящая категория')