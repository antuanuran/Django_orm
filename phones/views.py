import csv
from .models import Phone
from django.utils.text import slugify
from datetime import datetime

from django.shortcuts import render, redirect


with open('phones.csv', 'r', encoding='utf-8') as fd:
    phones = list(csv.DictReader(fd, delimiter=';'))


def index(request):

    for phonchik in phones:
        slug = slugify(phonchik.get('name'))
        time_bad_format = phonchik["release_date"]
        time_result = datetime.strptime(time_bad_format, '%d.%m.%Y')

        Phone.objects.create(name=f'{phonchik["name"]}', price=f'{phonchik["price"]}', image=f'{phonchik["image"]}', release_date=f'{time_result}', lte_exists=f'{phonchik["lte_exists"]}', slug=slug)

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




