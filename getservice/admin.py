from django.contrib import admin
from .models import Quote

# Register your models here.

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('response_id', 'client_name', 'client_email' , 'mobile' , 'location_type', 'area_m2', 'qty_bedroom', 'qty_living', 'qty_bathroom', 'window', 'qty_window' , 'kitchen' , 'kitchen_addon', 'bedroom_addon', 'living_addon', 'last_clean' , 'pets', 'best_time','address')
    list_filter = ('timestamp', 'location_type')
    readonly_fields = ('timestamp', 'response_id')

admin.site.register(Quote, QuoteAdmin)
