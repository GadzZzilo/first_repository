from django.db import models


class Human(models.Model):
    name = models.CharField(max_length=50, verbose_name='Полное имя')
    age = models.PositiveIntegerField(verbose_name='Возраст')
    work = models.CharField(max_length=100, verbose_name='Место работы')
    married = models.BooleanField(verbose_name='Женат/Замужем')
    slug = models.SlugField(max_length=100, verbose_name='URL')
    description = models.TextField(max_length=250, verbose_name='Описание')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
        ordering = ['name']

    def __str__(self):
        return self.name



