from django.shortcuts import render
from main.models import Container, Item
from main.forms import ItemForm, ContainerForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
import datetime

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    containers = Container.objects.filter(user=request.user)
    total_item = len(Item.objects.filter(user=request.user))

    context = {
        'name': 'Farrell Muhammad Hanau',
        'class': 'PBP-C',
        'shipper': request.user.username,
        'containers': containers,
        'last_login': request.COOKIES['last_login'],
        'total_item': total_item
    }

    return render (request, 'main.html', context)

def create_item(request):
    form = ItemForm(request)

    if form.is_valid() and request.method == "POST":
        container = form.save(commit=False)
        container.user = request.user
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form': form, 'shipper':request.user.username}
    return render(request, "create_item.html", context)

def create_container(request):
    form = ContainerForm(request.POST or None)
    isAlreadyExist = False
    if form.is_valid() and request.method == "POST":
        name = form.cleaned_data['name']
        if (name not in [container.name for container in Container.objects.filter(user=request.user)]):
            item = form.save(commit=False)
            item.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))
        isAlreadyExist = True

    
    context = {'form': form, 'exist':form.is_valid(), 'shipper':request.user.username}
    return render(request, "create_container.html", context)

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        
    context = {'form':form, 'shipper':request.user.username}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {'shipper':request.user.username}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@require_http_methods(["POST"])
def increment_item(request, id):
    item = Item.objects.get(id=id)
    if request.user == item.user:
        prev = item.amount
        item.amount += 1
        item.weight = round(item.weight/prev * item.amount, 2)
        item.save()

    return HttpResponseRedirect(reverse('main:show_main'))

@require_http_methods(["POST"])
def decrement_item(request, id):
    item = Item.objects.get(id=id)
    if request.user == item.user:
        if item.amount > 1:
            prev = item.amount
            item.amount -= 1
            item.weight = round(item.weight/prev * item.amount, 2)
            item.save()
        
    return HttpResponseRedirect(reverse('main:show_main'))

@require_http_methods(["POST"])
def remove_item(request, id):
    item = Item.objects.get(id=id)
    if request.user == item.user:
        item.delete()

    return HttpResponseRedirect(reverse('main:show_main'))

def edit_item(request, id):
    item = Item.objects.get(pk = id)

    form = ItemForm(request, instance=item)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form,  'shipper':request.user.username}
    return render(request, "edit_item.html", context)