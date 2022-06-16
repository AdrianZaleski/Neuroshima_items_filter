import random

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView

from .models import Ranged, Ammo
from .filters import RangedFilter

def index(request):
    return render(request, 'items/index.html')


def ranged_all(request):
    guns = Ranged.objects.all()
    my_filter = RangedFilter(request.GET, queryset=guns)
    guns = my_filter.qs
    
    page = request.GET.get('page', 1)
    paginator = Paginator(guns, 10)
    page_range = paginator.get_elided_page_range(number=page, on_each_side=3, on_ends=2)
    
    try:
        guns = paginator.page(page)
    except PageNotAnInteger:
        guns = paginator.page(1)
    except EmptyPage:
        guns = paginator.page(paginator.num_pages)
    
    context = {'list_of_guns': guns, 'my_filter': my_filter}
    return render(request, 'items/all_ranged.html', context)


def randomized_ranged_weapons(request):
    guns = Ranged.randomizer()
    return render(request, 'items/randomizer_weapon.html', {"list_of_guns" : guns})


class RangedDetailView(DetailView):
    template_name = 'items/detail_ranged.html'
    model = Ranged


def ammo_all(request):
    ammo = Ammo.objects.all()
    context = {'list_of_ammo': ammo}
    return render(request, 'items/all_ammo.html', context)


def randomized_ammo(request):
    ammunition = Ammo.randomizer()
    return render(request, 'items/randomizer_ammo.html', {"list_of_ammo" : ammunition})


class AmmoDetailView(DetailView):
    template_name = 'items/detail_ammo.html'
    model = Ammo
