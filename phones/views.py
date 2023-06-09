from .models import Phone

from django.shortcuts import render, redirect



def index(request):
    context = {'phones': Phone.objects.all()}
    return redirect('catalog')


def show_catalog(request):
    value_var = request.GET.get('sort')

    page_sort = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price'
                }.get(value_var, 'name')

    context = {'phones': Phone.objects.order_by(page_sort).all()}

    return render(request, 'catalog.html', context)


def show_product(request, slug):
    context = {'phone': Phone.objects.get(slug=slug)}
    return render(request, 'product.html', context)




