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
    rand_num = random.randrange(0, 100)

    ranged = Ranged.objects.filter(availability__gte=rand_num)
    context = {'ranged': ranged, 'rand_num': rand_num}

    return render(request, 'items/randomizer_test.html', context)

