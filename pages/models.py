from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Page(models.Model):
    title_page = models.CharField(max_length=50, verbose_name='Названия страницы')
    
    def __str__(self):
        return self.title_page
    
    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'


class Description(models.Model):
    
    title_description = models.CharField(max_length=50, verbose_name='Название описания')
    title = models.CharField(verbose_name='Заголовок описания', max_length=50, blank=True)
    text = RichTextField(verbose_name='Текст описания', blank=True)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, verbose_name='Страница', null=True)
    
    def __str__(self):
        return f'{self.title_description}' 
    
    class Meta:
        verbose_name = 'Описания'
        verbose_name_plural = 'Описании'
    

        

class Image(models.Model):
 
    
    title_image = models.CharField(max_length=50, verbose_name='Названия изображения')
    image_jpg = models.ImageField(upload_to="sliderimg/", verbose_name='Изображения JPG', blank=True)
    image_webp = models.ImageField(upload_to="slidrimg/", verbose_name="Изображения WEBP", blank=True)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, verbose_name='Страница', null=True)
    
    def __str__(self):
        return self.title_image
    
    class Meta:
        verbose_name = 'Изображения'
        verbose_name_plural = 'Изображении'



class Slider(models.Model):
    title_slider = models.CharField(max_length=50, verbose_name='Названия слайдера')
    images = models.ManyToManyField(Image, verbose_name='Изображения', blank=True)
    description = models.ManyToManyField(Description, verbose_name='Описания', blank=True)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, verbose_name='Страница', null=True)
    
    def __str__(self):
        return self.title_slider
    
    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'
                    
        
                
    
