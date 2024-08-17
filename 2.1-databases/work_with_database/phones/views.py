from django.shortcuts import render, redirect, get_object_or_404
from .models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    phones = Phone.objects.all()
    template = 'catalog.html'
    sort_by = request.GET.get('sort')

    if sort_by == 'name':
        phones = Phone.objects.all().order_by('name')
    elif sort_by == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif sort_by == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    else:
        phones = Phone.objects.all()

    context = {
        'phones': phones,
        'sort_by': sort_by
    }
    return render(request, template, context)


def show_product(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    template = 'product.html'
    context = {
        'phone': phone
    }
    return render(request, template, context)
