from django.contrib import admin

# Register your models here.
from .models import Pet
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
 list_display=('id','name','price','slug','gender','animal_type','breed','age','description')

#admin.site.register(Pet,PetAdmin)

