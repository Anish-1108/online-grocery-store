from django.contrib import admin
from .models import*

# Register your models here.

admin.site.register(User)
admin.site.register(Add_product)
admin.site.register (Add_to_cart)
admin.site.register(maincatagory)
admin.site.register(Address)