from django.contrib import admin
from myApp.models import *

class Customer_User_Display(admin.ModelAdmin):
    list_display=['display_name','email','User_type']

admin.site.register(Custom_User,Customer_User_Display)
