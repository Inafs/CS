from django.shortcuts import render
from .forms import OrderForm
from .models import IndexSlider, UpCard, DownCards, Order

# Create your views here.
def first_page(request):
    description_up = UpCard.objects.get(pk=1)
    slider_index = IndexSlider.objects.all()
    desc_1 = DownCards.objects.get(pk=1)
    desc_2 = DownCards.objects.get(pk=2)
    desc_3 = DownCards.objects.get(pk=3)
    form = OrderForm()
    dict_obj = { 'slider_index': slider_index,
                                              'description_up': description_up,
                                              'desc_1': desc_1,
                                              'desc_2': desc_2,
                                              'desc_3': desc_3,
                                              'form': form}

    if request.POST:
        name = request.POST['name']
        phone = request.POST['order_phone']
        mail = request.POST['mail']
        text = request.POST['text']
        element = Order(order_name = name, order_phone = phone, order_mail = mail, order_text = text)
        element.save()
    return render(request, './index.html', dict_obj)

