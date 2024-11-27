from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Listing, ListingAdmin)
