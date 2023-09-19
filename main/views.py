from django.shortcuts import render
from main.models import Container, Item
from main.forms import ItemForm, ContainerForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core import serializers

# Create your views here.
def show_main(request):
    containers = Container.objects.all()
    context = {
        'name': 'Farrell Muhammad Hanau',
        'class': 'PBP-C',
        'shipper': 'EfEmEitch Express',
        'containers': containers

    }

    return render (request, 'main.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form': form}
    return render(request, "create_item.html", context)

def create_container(request):
    form = ContainerForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        name = form.cleaned_data['name']
        if (name not in [container.name for container in Container.objects.all()]):
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form': form}
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
