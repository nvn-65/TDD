from django.shortcuts import render, redirect
from lists.models import Item, List


def new_list(request):
    """новый список"""
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/один-единственный/')


def home_page(request):
    """Домашняя страница"""
    return render(request, 'home.html')


def view_list(request):
    """новый спмсок"""
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
