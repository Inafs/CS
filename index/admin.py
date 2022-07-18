from django.contrib import admin
from .models import IndexSlider, Order, UpCard, DownCards

# Register your models here.
admin.site.register(IndexSlider)
admin.site.register(Order)
admin.site.register(UpCard)
admin.site.register(DownCards)

