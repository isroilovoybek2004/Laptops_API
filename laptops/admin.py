from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Laptops, Manufacturer, LaptopReview
# Register your models here.


# class BookAuthorModelAdmin(admin.ModelAdmin):
#     search_fields = ['book.title', 'author.name']
#     list_display = ['book.title','author.name','create_at']
#     list_filter = ['book.title', 'author.name','create_at']


class LaptopModelAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description', 'manufacturer']
    list_display = ['name', 'manufacturer']
    list_filter = ['create_at']


admin.site.register(Laptops, LaptopModelAdmin)
admin.site.register(Manufacturer)
admin.site.register(LaptopReview)
# admin.site.register(Laptops)