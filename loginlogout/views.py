from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.
def login(request):
    if request.POST:
        login = request.POST['login']
        password = request.POST['password']
        user = auth.authenticate(password=password, username=login)
        if user:
            auth.login(request, user)
        else:
            u = User(username=login, password=password)
            u.save()
            auth.login(request, u)
        print(login, password)
        return redirect('/video/hello/')
    else:
        response = csrf(request)
        return render(request, './form.html', response)


def out(request):
    #print(request.user)
    auth.logout(request)
    return redirect('/video/hello/')