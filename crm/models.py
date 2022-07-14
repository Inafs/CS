from django.db import models

class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')
    order_mail = models.CharField(max_length=200, verbose_name='Почта')
    order_text = models.TextField(max_length=1000, verbose_name='Сообщение')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявки'