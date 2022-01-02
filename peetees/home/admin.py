from django.contrib import admin
from .models import Vegetable,Grocery,Stationary,Dairy,Electrical,Bakery,Fruit

# Register your models here.

admin.site.register(Vegetable)
admin.site.register(Fruit)
admin.site.register(Grocery)
admin.site.register(Stationary)
admin.site.register(Dairy)
admin.site.register(Electrical)
admin.site.register(Bakery)