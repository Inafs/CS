from django.shortcuts import render
from .models import Description, Slider
from fos.forms import OrderForm

# Create your views here.
def first_page(request):
    sliders = Slider.objects.filter(page=2)
    desc = Description.objects.filter(page=2)
    form = OrderForm(request.POST or None)

    context = {
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