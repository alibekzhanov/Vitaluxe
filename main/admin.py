from django.contrib import admin
from .models import Advertisement, Product


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'ratings')
    search_fields = ('name',)
    list_filter = ('price',)


admin.site.register(Advertisement, AdvertisementAdmin)
admin.site.register(Product, ProductAdmin)
