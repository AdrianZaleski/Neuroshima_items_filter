import random

# Create your views here.
from django.shortcuts import render
from django.views import generic


from .models import Ranged, Difficulty, Ammo


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
    difficulty = Difficulty.objects.all()
    context = {"difficulty": difficulty}
    return render(request, 'items/index.html', context)


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
