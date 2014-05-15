import autocomplete_light

from cities_light.models import City

class CityAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields=('search_names',)
    autocomplete_js_attributes={'placeholder': 'city name ..'}

autocomplete_light.register(City, CityAutocomplete)
