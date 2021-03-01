from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import EatModel
from django.contrib.auth.decorators import login_required

from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.db.models import Q

# Create your views here.


def registfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return redirect('login')
        except IntegrityError:
            return render(request, 'regist.html', {'error':'このユーザーは既に登録されています。'})
    return render(request, 'regist.html', {})

def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('create')
        else:
            return render(request, 'login.html', {})
    return render(request, 'login.html', {})

def mainfunc(request):
    if request.method == "POST":
        query = request.POST.get('aim')
        data_list = EatModel.objects.filter(Q(readtext__icontains=query) | Q(title__icontains=query))
        return render(request, 'view.html', {'data_list':data_list})
    object_list = EatModel.objects.all()
    return render(request, 'main.html', {'object_list':object_list})

def logoutfunc(request):
    logout(request)
    return redirect('login')

def detailfunc(request, pk):
    object = get_object_or_404(EatModel, pk=pk)
    return render(request, 'detail.html', {'object':object})

def goodfunc(request, pk):
    object = EatModel.objects.get(pk=pk)
    object.good = object.good + 1
    object.save()
    return redirect('')

def readfunc(request, pk):
    object= EatModel.objects.get(pk=pk)
    username = request.user.get_username()
    if username in object.readtext:
        return redirect('')
    else:
        object.read = object.read + 1
        object.readtext = object.readtext + ' ' + username
        object.save()
        return redirect('')

class EatCreate(CreateView):
    template_name = 'create.html'
    model = EatModel
    fields = ('title', 'content', 'author', 'snsimage', 'readtext', 'material')
    success_url = reverse_lazy('create')

def viewfunc(request):
    if request.method == "POST":
        query = request.POST.get('aim')
        data_list = EatModel.objects.filter(readtext__icontains=query)
        return render(request, 'main.html', {'data_list':data_list})
    object_list = EatModel.objects.all()
    return render(request, 'view.html', {'object_list':object_list})