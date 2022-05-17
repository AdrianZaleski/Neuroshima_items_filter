import random

# Create your views here.
from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Ranged, Difficulty, Ammo
from .filters import RangedFilter

# As a standoff function - to much recursion occurs:
# USe as a copy to modify in each view separate.
# def randomizer(request):
#     guns = Ranged.objects.all()
#     list_of_guns = []
#     for gun in guns:
#         rand_num = random.randrange(0, 100)
#         if gun.availability >= rand_num:
#
#             list_of_guns.append(gun)
#     context = {'list_of_guns': list_of_guns}
#
#     return render(request, 'items/randomizer_weapon.html', context)


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
    guns = Ranged.objects.all()
    list_of_guns = []
    for gun in guns:
        rand_num = random.randrange(0, 100)
        if gun.availability >= rand_num:

            list_of_guns.append(gun)
    context = {'list_of_guns': list_of_guns}

    return render(request, 'items/randomizer_weapon.html', context)


def detail_ranged(request, id_code):
    ranged = Ranged.objects.get(id_code=id_code)
    context = {'ranged': ranged}
    return render(request, 'items/detail_ranged.html', context)


def ammo_all(request):
    ammo = Ammo.objects.all()
    context = {'list_of_ammo': ammo}
    return render(request, 'items/all_ammo.html', context)


def randomized_ammo(request):
    ammunition = Ammo.objects.all()
    list_of_ammo = []
    for ammo in ammunition:
        rand_num = random.randrange(0, 100)
        if ammo.availability >= rand_num:
            list_of_ammo.append(ammo)
    context = {'list_of_ammo': list_of_ammo}

    return render(request, 'items/randomizer_ammo.html', context)


def detail_ammo(request, id_code):
    ammo = Ammo.objects.get(id_code=id_code)
    context = {'ammo': ammo}
    return render(request, 'items/detail_ammo.html', context)
