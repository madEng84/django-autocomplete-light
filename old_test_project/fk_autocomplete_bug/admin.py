from django.contrib import admin

import autocomplete_light

from models import Address
from .forms import AddressForm

class AddressAdmin(admin.ModelAdmin):
    form = AddressForm #autocomplete_light.modelform_factory(Address)

admin.site.register(Address, AddressAdmin)
