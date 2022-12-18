from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

# from .models import Question

def index(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'shop/index.html', context)

def show(request, id):
    product = Product.objects.get(id=id)
    context = {
        'product': product
    }
    return render(request, 'shop/products.html', context)

def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        products = Product.objects.all()
        return render(request, 'shop/products.html', {'products': products})
    else:
        form = ProductForm()
    return render(request, 'shop/create.html', {'form': form})

def update(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('../../shop')
    context = {'form': form}
    return render(request, 'shop/update.html', context)

def delete(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('../../shop')
    context = {'item': product}
    return render(request, 'shop/delete.html', context)