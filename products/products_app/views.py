from django.shortcuts import render, get_object_or_404, redirect

from products_app.models import Products
from products_app.forms import ProductsForm, ProductsDeleteForm


def index_view(request):
    products = Products.objects.all().exclude(remainder=0).order_by('category', 'name')
    return render(request, 'index.html', context={'products': products})


def products_view(request, id):
    products = get_object_or_404(Products, id=id)
    return render(request, 'products_view.html', context={'products': products})


def products_create_view(request):
    if request.method == "GET":
        form = ProductsForm()
        return render(request, 'products_create.html', context={'form': form})
    elif request.method == "POST":
        form = ProductsForm(data=request.POST)
        if form.is_valid():
            product = Products.objects.create(
                name=form.cleaned_data.get('name'),
                text=form.cleaned_data.get('text'),
                category=form.cleaned_data.get('category'),
                remainder=form.cleaned_data.get('remainder'),
                cost=form.cleaned_data.get('cost'),
            )
            return redirect('index_view')
        return render(request, 'products_create.html', context={'form': form})


def products_update_view(request, id):
    product = get_object_or_404(Products, id=id)

    if request.method == 'GET':
        form = ProductsForm(initial={
            'name': product.name,
            'text': product.text,
            'category': product.category,
            'remainder': product.remainder,
            'cost': product.cost,
        })
        return render(request, 'products_update.html', context={'form': form, 'product': product})
    elif request.method == 'POST':
        form = ProductsForm(data=request.POST)
        if form.is_valid():
            product.name = form.cleaned_data.get("name")
            product.text = form.cleaned_data.get("text")
            product.category = form.cleaned_data.get("category")
            product.remainder = form.cleaned_data.get("remainder")
            product.cost = form.cleaned_data.get("cost")
            product.save()
            return redirect('index_view')

        return render(request, 'products_update.html', context={'form': form, 'product': product})


def products_delete_view(request, id):
    product = get_object_or_404(Products, id=id)

    if request.method == 'GET':
        form = ProductsDeleteForm()
        return render(request, 'products_delete.html', context={'product': product, 'form': form})
    elif request.method == 'POST':
        form = ProductsDeleteForm(data=request.POST)
        if form.is_valid():
            if form.cleaned_data['name'] != product.name:
                form.errors['name'] = ['Названия статей не совпадают']
                return render(request, 'products_delete.html', context={'product': product, 'form': form})

            product.delete()
            return redirect('index_view')
        return render(request, 'products_delete.html', context={'product': product, 'form': form})