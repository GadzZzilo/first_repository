from ckeditor.fields import RichTextField
from django.db import models
from django.utils.safestring import mark_safe


class Developer(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=50)
    age = models.PositiveIntegerField(verbose_name='Возраст')
    slug = models.SlugField(verbose_name='URL')
    photo = models.ImageField(verbose_name='Фото', upload_to='authors_photos')
    description = RichTextField(verbose_name='Описание')
    services = models.ManyToManyField('Service', verbose_name='Услуги')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Разработчик'
        verbose_name_plural = 'Разработчики'
        ordering = ['name']


class Service(models.Model):
    name = models.CharField(max_length=70, verbose_name='Название')
    description = RichTextField(verbose_name='Описание')
    slug = models.SlugField(verbose_name='URL')
    image = models.ImageField(verbose_name='Картинка', upload_to='services_images/')
    author = models.ManyToManyField('Developer', verbose_name='Автор', blank=True, null=True)
    price = RichTextField(verbose_name='Прайслист')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['name']

    def __str__(self):
        return self.name


class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(max_length=100, verbose_name='Электронная почта')
    message = models.TextField(verbose_name='Отзыв')
    create_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['name']
