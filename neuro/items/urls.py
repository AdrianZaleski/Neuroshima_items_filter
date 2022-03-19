from django.urls import path
from . import views


app_name = 'items'

urlpatterns = [
    path('', views.index, name='index'),

    path('ranged/', views.ranged_all, name='all_ranged'),
    path('ranged/random/', views.randomized_ranged_weapons, name='random_ranged'),
    path('ranged/detail/<str:id_code>', views.detail_ranged, name='detail_ranged'),

    path('ammo/', views.ammo_all, name='all_ammo'),
    path('ammo/random/', views.randomized_ammo, name='random_ammo'),
    path('ammo/detail/<str:id_code>', views.detail_ammo, name='detail_ammo'),

]

