from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from product.models import Category
from user.models import UserProfile


def index(request):
    return HttpResponse("Hello world its user page mf")


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
    category = Category.objects.all()
    context = {
        'category': category
    }
    return render(request, 'signup_form.html', context)


def logout_func(request):
    logout(request)
    return HttpResponseRedirect('/')