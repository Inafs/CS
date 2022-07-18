from django.db import models

# Create your models here.
class IndexSlider(models.Model):
    index_img_jpeg = models.ImageField(upload_to='sliderimg/')
    index_img_webp = models.ImageField(upload_to='sliderimg/')
    

    class Meta:
        verbose_name = 'Слайд для главной'
        verbose_name_plural = 'Слайды для главной'


class UpCard(models.Model):
    desc_head = models.CharField(max_length=500, verbose_name='Верхнее описание')
    desc_mid = models.CharField(max_length=500, verbose_name='Срединное описание')
    desc_bot = models.CharField(max_length=500, verbose_name='Нижнее описание')

    def __str__(self):
        return self.desc_head

    class Meta:
        verbose_name = 'Описание для верха'
        verbose_name_plural = 'Описание для верха'


class DownCards(models.Model):
    desc_up = models.CharField(max_length=500, verbose_name='Верхнее описание')
    desc_down = models.CharField(max_length=500, verbose_name='Нижнее описание')

    def __str__(self):
        return self.desc_up

    class Meta:
        verbose_name = 'Описание для нижних карточек'
        verbose_name_plural = 'Описание для нижних карточек'


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