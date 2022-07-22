from django.shortcuts import render
from .models import Description, Slider
from fos.forms import OrderForm

# Create your views here.
def first_page(request):
    sliders = Slider.objects.filter(page=2)
    
    index_slider = Slider.objects.get(page=2, title_slider="Слайдер для главной")
    end_slider = Slider.objects.get(page=2, title_slider="Нижний Слайдер")
    
    sliders = sliders.exclude(title_slider="Нижний Слайдер")
    sliders = sliders.exclude(title_slider="Слайдер для главной")
    
    desc = Description.objects.filter(page=2)
    form = OrderForm(request.POST or None)

    context = {
        'index_slider': index_slider,
        'end_slider': end_slider,
        'sliders': sliders,
        'form': form,
        'desc': desc,
    }

    if request.method == "POST" and form.is_valid():
        name = form.cleaned_data['name']
        mail = form.cleaned_data['mail']
        phone = form.cleaned_data['phone']
        text = form.cleaned_data['text']

        new_form = form.save()
             

    return render(request, './index.html', context)


def news_page(request):
    sliders = Slider.objects.filter(page=1)
    form = OrderForm(request.POST or None)
        
    context = {
        'sliders': sliders,
        'form': form,
    }

    if request.method == "POST" and form.is_valid():
        name = form.cleaned_data['name']
        mail = form.cleaned_data['mail']
        phone = form.cleaned_data['phone']
        text = form.cleaned_data['text']

        new_form = form.save()

    
    return render(request, 'list.html', context)