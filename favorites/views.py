from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from favorites.models import FavoriteCart, FavoriteCartForm
from order.models import ShopCart
from product.models import Category


def index(request):
    return HttpResponse("hello")

@login_required(login_url='/login')  # Check login
def addtofavoritecart(request, id):
    url = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user  # Access User Session information
    checkproduct = FavoriteCart.objects.filter(product_id=id)

    if checkproduct:
        control = 1  # The product is in the cart
    else:
        control = 0  # The product is not in the cart"""

    if request.method == 'POST':  # if there is a post
        form = FavoriteCartForm(request.POST)
        if form.is_valid():
            if control == 1:  # Update  shopcart
                data = FavoriteCart.objects.get(product_id=id)
                data.quantity += form.cleaned_data['product']
                data.save()
            else:
                data = FavoriteCart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['product']
                data.save()
        messages.success(request, "Product added to FavoriteCart ")
        return HttpResponseRedirect(url)

    else:  # if there is no post
        if control == 1:  # Update  shopcart
            data = FavoriteCart.objects.get(product_id=id)
            data.save()  #
        else:  # Inser to Shopcart
            data = FavoriteCart()  # model ile bağlantı kur
            data.user_id = current_user.id
            data.product_id = id
            data.save()  #
        messages.success(request, "Product added to FavoriteCart")
        return HttpResponseRedirect(url)


def favoritecart(request):
    category = Category.objects.all()
    current_user = request.user
    favoritecart = FavoriteCart.objects.filter(user_id=current_user.id)
    shopcart = ShopCart.objects.filter(user_id=current_user.id)

    total = 0
    for i in shopcart:
        total += i.product.price * i.quantity

    context = {
        'favoritecart': favoritecart,
        'category': category,
        'shopcart': shopcart,
        'total': total,

    }
    return render(request, 'favorites_products.html', context )


@login_required(login_url='/login')  # Check login
def deletefromfavoritecart(request, id):
    FavoriteCart.objects.filter(id=id).delete()
    messages.success(request, "Your item deleted from Favoritecart.")
    return HttpResponseRedirect("/favoritecart/")

