from django.contrib import admin

from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display =['name', 'slug',]
	prepopulated_fields = {'slug':('name',)}

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
	list_display =['name', 'price',]
	prepopulated_fields = {'slug':('name',)}
	
