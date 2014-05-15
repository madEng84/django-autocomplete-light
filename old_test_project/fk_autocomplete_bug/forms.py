# -*- coding: utf-8 -*-
from django import forms
from .models import Address
from cities_light.models import City
import autocomplete_light
class AddressForm(forms.ModelForm):
    
    city = forms.ModelChoiceField(City.objects.all(),
                                   widget=autocomplete_light.ChoiceWidget('CityAutocomplete')
                                   )
    
    class Meta:
        model=Address