from django.urls import path
from . import views

app_name = 'items'
urlpatterns = [
    path('', views.index, name='index'),
    path('random_ranged', views.randomized_ranged_weapons, name='random ranged weapons'),
    path('ranged_detail/<str:id_code>', views.ranged_detail, name='ranged_detail'),

]
