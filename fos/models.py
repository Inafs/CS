from django.db import models

# Create your models here.
class Order(models.Model):
    dt = models.DateTimeField(auto_now=True, verbose_name='Дата')
    name = models.CharField(max_length=100, verbose_name='Имя')
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    mail = models.EmailField(blank=True, null=True, verbose_name='Почта')
    text = models.TextField(max_length=1000,blank=True, null=True, verbose_name='Сообщение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вопросы клиентов'
        verbose_name_plural = 'Обратная связь'