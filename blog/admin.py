from django.contrib import admin
from .models import * 
 #to import all the models in the models class otherwise we would have to do that seperately 

# Register your models here.
admin.site.register(Post)  #to see them in the admin console 
