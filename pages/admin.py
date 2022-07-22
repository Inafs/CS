from django.contrib import admin

from .models import Description, Image, Slider, Page 

# Register your models here.

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title_page", )
    ordering = ("title_page", )

@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    list_display = ("title_description", "page", )
    ordering = ("page", )
    list_filter = ("page", )
    search_fields = ("page", )
    


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("title_image", "page",)
    ordering = ("page", )
    list_filter = ("page", )
    search_fields = ("title_image", "page", )
    

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ("title_slider", "page", )
    ordering = ("title_slider", "page", )
    list_filter = ("page", )
    search_fields = ("title_slider", "page", )