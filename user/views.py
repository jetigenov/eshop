from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from order.models import Order, ShopCart, OrderProduct
from product.models import Category
from user.forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from user.models import UserProfile



@login_required(login_url='/login')
def index(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    shopcart = ShopCart.objects.filter(user_id=current_user.id)

    total = 0
    for i in shopcart:
        total += i.product.price * i.quantity

    context = {
        'category': category,
        'profile': profile,
        'shopcart': shopcart,
        'total': total,

    }
    return render(request, 'user_profile.html', context)

def login_form(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user = request.user
            userprofile = UserProfile.objects.get(user_id=current_user.id)
            request.session['userimage'] = userprofile.image.url
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "There was a problem!!! Your username or password is incorrect.")
            return HttpResponseRedirect('/login')

    category = Category.objects.all()
    context = {
        'category': category
     }
    return render(request, 'login_form.html', context)



def signup_form(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # Create data in profile table for user
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = "images/users/user.png"
            data.save()
            messages.success(request, 'Your account has been created!')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('/signup')

    form = SignUpForm()
    category = Category.objects.all()
    context = {'form': form,
               'category': category,
               }
    return render(request, 'signup_form.html', context)


def logout_func(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url='/login')
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user) # request.user is user  data
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return HttpResponseRedirect('/user')
    else:
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile) #"userprofile" model -> OneToOneField relatinon with user
        current_user = request.user
        shopcart = ShopCart.objects.filter(user_id=current_user.id)

        total = 0
        for i in shopcart:
            total += i.product.price * i.quantity

        context = {
            'category': category,
            'user_form': user_form,
            'profile_form': profile_form,
            'shopcart': shopcart,
            'total': total,

        }
        return render(request, 'user_update.html', context)


@login_required(login_url='/login') # Check login
def user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request, 'Please correct the error below.<br>'+ str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        current_user = request.user
        shopcart = ShopCart.objects.filter(user_id=current_user.id)

        total = 0
        for i in shopcart:
            total += i.product.price * i.quantity

        return render(request, 'user_password.html', {'form': form, 'category': category, 'shopcart': shopcart, 'total': total})



@login_required(login_url='/login') # Check login
def user_orders(request):
    category = Category.objects.all()
    current_user = request.user
    orders = Order.objects.filter(user_id=current_user.id)
    shopcart = ShopCart.objects.filter(user_id=current_user.id)

    total = 0
    for i in shopcart:
        total += i.product.price * i.quantity

    context = {'category': category,
               'orders': orders,
               'shopcart': shopcart,
               'total': total,
               }
    return render(request, 'user_orders.html', context)
