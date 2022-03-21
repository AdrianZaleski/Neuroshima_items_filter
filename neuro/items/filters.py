import django_filters
from django_filters import CharFilter
from django import forms

from .models import *

class RangedFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr="icontains", label="Name")
    weapon_class = django_filters.ModelMultipleChoiceFilter(queryset=Weapon.objects.all(),
        widget=forms.CheckboxSelectMultiple()
        )
    ammo = django_filters.ModelMultipleChoiceFilter(queryset=Ammo.objects.all(),
        widget=forms.CheckboxSelectMultiple()
        )
    class Meta:
        model = Ranged
        fields = ['name', 'weapon_class', 'ammo']
