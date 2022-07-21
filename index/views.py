from django.shortcuts import render
from fos.forms import OrderForm
from .models import IndexSlider, UpCard, DownCards

# Create your views here.
def first_page(request):
    description_up = UpCard.objects.get(pk=1)
    slider_index = IndexSlider.objects.all()
    desc_1 = DownCards.objects.get(pk=1)
    desc_2 = DownCards.objects.get(pk=2)
    desc_3 = DownCards.objects.get(pk=3)
    form = OrderForm(request.POST or None)
    dict_obj = { 'slider_index': slider_index,
                                              'description_up': description_up,
                                              'desc_1': desc_1,
                                              'desc_2': desc_2,
                                              'desc_3': desc_3,
                                              'form': form}

    if request.method == "POST" and form.is_valid():
        name = form.cleaned_data['name']
        mail = form.cleaned_data['mail']
        phone = form.cleaned_data['phone']
        text = form.cleaned_data['text']

        new_form = form.save()
             

    return render(request, './index.html', dict_obj)

