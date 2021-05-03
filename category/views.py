from django.shortcuts import render

from .models import Category

from images.models import Images


def category_list(request):
    cat=Category.objects.all()
    return render(request,'category/category.html',{'category':cat})

def category(request,slug):
    image=Images.objects.filter( category__slug__contains= slug)
    data={}
    data['category']=image
    data['title']=slug
    return render(request,'category/category_detail.html',data  )