from django.db import models

# Create your models here.
class Product(models.Model ):
   product_name = models.CharField(max_length=50)
   mrp = models.IntegerField()
   id = models.IntegerField(primary_key=True)
   our_price = models.IntegerField()

   def __str__(self):
      return f"{self.product_name} \t @Rs {self.our_price }"

class Grocery(models.Model ):
   grocery_name = models.CharField(max_length=50)
   grocery_mrp = models.IntegerField()
   grocery_id = models.IntegerField(primary_key=True)
   grocery_price = models.IntegerField()

   def __str__(self):
      return f"{self.grocery_name} \t @Rs {self.grocery_price }"

class Bakery(models.Model ):
   bakery_name = models.CharField(max_length=50)
   bakery_mrp = models.IntegerField()
   bakery_id = models.IntegerField(primary_key=True)
   bakery_price = models.IntegerField()

   def __str__(self):
      return f"{self.bakery_name} \t @Rs {self.bakery_price }"

class Dairy(models.Model ):
   dairy_name = models.CharField(max_length=50)
   dairy_mrp = models.IntegerField()
   dairy_id = models.IntegerField(primary_key=True)
   dairy_price = models.IntegerField()

   def __str__(self):
      return f"{self.dairy_name} \t @Rs {self.dairy_price }"

class Electrical(models.Model ):
   electrical_name = models.CharField(max_length=50)
   electrical_mrp = models.IntegerField()
   electrical_id = models.IntegerField(primary_key=True)
   electrical_price = models.IntegerField()

   def __str__(self):
      return f"{self.electrical_name} \t @Rs {self.electrical_price }"

class Stationary(models.Model ):
   stationary_name = models.CharField(max_length=50)
   stationary_mrp = models.IntegerField()
   stationary_id = models.IntegerField(primary_key=True)
   stationary_price = models.IntegerField()

   def __str__(self):
      return f"{self.stationary_name} \t @Rs {self.stationary_price }"