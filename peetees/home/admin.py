from django.contrib import admin
from .models import Product,Grocery,Stationary,Dairy,Electrical,Bakery

# Register your models here.

admin.site.register(Product)
admin.site.register(Grocery)
admin.site.register(Stationary)
admin.site.register(Dairy)
admin.site.register(Electrical)
admin.site.register(Bakery)