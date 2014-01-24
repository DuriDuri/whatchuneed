from django.contrib import admin
from .models import Offer

class OfferAdmin(admin.ModelAdmin):
    class Meta:
        model = Offer
        

admin.site.register(Offer, OfferAdmin)