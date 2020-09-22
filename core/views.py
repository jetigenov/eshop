# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from core.forms import SearchForm
from core.models import Setting, ContactForm, ContactMessage
from order.models import ShopCart
from product.models import Category, Product, Images, Comment


def index(request):
    category = Category.objects.all()

    current_user = request.user  # Access User Session information
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for i in shopcart:
        total += i.product.price * i.quantity

    products_slider = Product.objects.all().order_by('id')[:4]
    products_latest = Product.objects.all().order_by('-id')[:4]
    products_picked = Product.objects.all().order_by('?')[:4]

    setting = Setting.objects.get(pk=1)
    page = "home"

    context = {
        'setting': setting,
        'page': page,
        'products_slider': products_slider,
        'products_latest': products_latest,
        'products_picked': products_picked,
        'category': category,
        'total': total,

    }
    return render(request, 'index.html', context)


def aboutus(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    current_user = request.user  # Access User Session information
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for i in shopcart:
        total += i.product.price * i.quantity

    context = {'setting': setting,
               'category': category,
               'total': total,

               }
    return render(request, 'about.html', context)


def contactus(request):
    if request.method == 'POST':  # check post
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()  # create relation with model
            data.name = form.cleaned_data['name']  # get form input data
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Your message has been sent! Thank you for your message.")
            return HttpResponseRedirect('/contact')

    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    form = ContactForm
    current_user = request.user  # Access User Session information
    shopcart = ShopCart.objects.filter(user_id=current_user.id)

    total = 0
    for i in shopcart:
        total += i.product.price * i.quantity

    context = {
        'setting': setting,
        'form': form,
        'category': category,
        'total': total,

    }
    return render(request, 'contact.html', context)


def category_products(request, id, slug):
    category = Category.objects.all()
    categories = Category.objects.get(pk=id)
    products = Product.objects.filter(category_id=id)

    current_user = request.user  # Access User Session information
    shopcart = ShopCart.objects.filter(user_id=current_user.id)

    total = 0
    for i in shopcart:
        total += i.product.price * i.quantity

    context = {
        'products': products,
        'category': category,
        'categories': categories,
        'total': total,

    }
    return render(request, 'category_products.html', context)


def search(request):
    if request.method == 'POST':  # check post
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']  # get form input data
            catid = form.cleaned_data['catid']
            if catid == 0:
                products = Product.objects.filter(title__icontains=query)  # SELECT * FROM product WHERE title LIKE '%query%'
            else:
                products = Product.objects.filter(title__icontains=query, category_id=catid)

            category = Category.objects.all()
            context = {'products': products, 'query': query,
                       'category': category,}
            return render(request, 'search_products.html', context)

    return HttpResponseRedirect('/')


def search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        products = Product.objects.filter(title__icontains=q)
        results = []
        for i in products:
            product_json = {}
            product_json = i.title
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def product_detail(request, id, slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id, status='True')

    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)

    products_picked = Product.objects.filter(category__product=product)[:4]


    total = 0
    for i in shopcart:
        total += i.product.price * i.quantity

    context = {
        'product': product,
        'category': category,
        'images': images,
        'comments': comments,
        'total': total,
        'products_picked': products_picked,

    }
    return render(request, 'product_detail.html', context)