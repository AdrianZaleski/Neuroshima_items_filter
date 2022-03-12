import random

# Create your views here.
from django.shortcuts import render
from django.views import generic


from .models import Ranged, Difficulty


def index(request):
    difficulty = Difficulty.objects.all()
    context = {"difficulty": difficulty}
    return render(request, 'items/index.html', context)


def randomizer(request):
    guns = Ranged.objects.all()
    list_of_guns = []

    for gun in guns:
        rand_num = random.randrange(0, 100)
        if gun.availability >= rand_num:
            list_of_guns.append(gun)

    context = {'list_of_guns': list_of_guns}

    return render(request, 'items/randomizer_test.html', context)
