from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Images

from django.views.generic.list import ListView
from hitcount.views import HitCountDetailView

import random
from taggit.models import Tag
from django.db.models import Q
class IndexView(ListView):

    template_name = 'images/images_list.html'
    model = Images
    context_object_name = 'images_list'
    queryset = Images.objects.filter(status=True).order_by('date')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        images=list(Images.objects.filter(status=True).order_by('date'))
        object_list=images[:5]
        random.shuffle(object_list)
        context['images_random'] =object_list 
        return context

    def get_queryset(self):
        result = super(IndexView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            q = Q()
            q = q | Q(title=query) | Q(tags__name__icontains=query)
            postresult=Images.objects.filter(q)
            
            result = postresult
        else:

            result = Images.objects.all()
        return result

class PostDetailView(HitCountDetailView):
    model = Images
    template_name = 'images/image_details.html'
    context_object_name = 'image'
    slug_field = 'slug'
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context.update({
        'popular_posts': Images.objects.order_by('-hit_count_generic__hits')[:3],
        })
        images=list(Images.objects.filter(status=True).order_by('date'))
        object_list=images[:10]
        random.shuffle(object_list)
        context['random'] =object_list
        
        return context


def tagged(request,slug):
    tag=get_object_or_404(Tag,slug=slug)
    print('tag{}'.format(tag))
    images=Images.objects.filter(tags=tag)
    print(images)
    return render(request,'images/images_list.html',{'images_list':images})
class PicDay(ListView):
    
    template_name = 'images/picofday.html'
    model = Images
    context_object_name = 'images_list'
    queryset = Images.objects.filter(pic_day=True).order_by('date')

def about(request):
    return render(request,'images/about.html')