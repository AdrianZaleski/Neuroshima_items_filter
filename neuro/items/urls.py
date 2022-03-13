from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('', views.index, name='index'),
    path('random/ranged/', views.randomized_ranged_weapons, name='random_ranged_weapons'),
    path('detail/ranged/<str:id_code>', views.detail_ranged, name='detail_ranged'),

    path('random/ammo/', views.randomized_ammo, name='random_ammo'),
    path('detail/ammo/<str:id_code>', views.detail_ammo, name='detail_ammo'),

]

