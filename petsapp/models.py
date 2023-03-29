from django.db import models
from django.db.models.signals import pre_save
from petsapp.utils import unique_slug_generator
from django.urls import reverse
from django.db.models import Q


# Create your models here.

  

class PetsQuerySet(models.QuerySet):
    def dog_list(self):
        return self.filter(animal_type='D')
    def cat_list(self):
        return self.filter(animal_type='C')
    def search(self, query):
        #print(query)
        lookups = (Q(name__icontains=query) | 
                  Q(animal_type__icontains=query) |
                  Q(breed__icontains=query)|Q(age__icontains=query)
                  | Q(tag__name__icontains=query)
                  )
        return self.filter(lookups)
    
class CustomManager(models.Manager):
  def get_queryset(self):	# overriding Built-in method called when we call all()
     return PetsQuerySet(self.model,using=self._db)


  def get_pets_price_range(self, r1, r2):
    return super().get_queryset().filter(price__range=(r1, r2))
  
  def search(self, query):
       # print(query)
        return self.get_queryset().search(query)
    
class Pet(models.Model):
    gender =(("male","male"),("female","female"))
    type=(("D","Dog"),("C","Cat"))
    image=models.ImageField(upload_to="media")
    name=models.CharField(max_length=30)
    price=models.FloatField(default="10")
    animal_type=models.CharField(max_length=30,choices=type)
    breed=models.CharField(max_length=30)
    age=models.IntegerField()
    gender=models.CharField(max_length=10,choices=gender)
    description=models.CharField(max_length=400)
    objects = models.Manager()			# Default Manager
    pets = CustomManager()# Custom Manager
    pet = PetsQuerySet.as_manager()
    slug = models.SlugField(max_length=30,null=True)

    class Meta:
        db_table = "Pets"


def pets_pre_save_receiver(sender, instance, *args, **kwargs):
    #print("pets_pre_save_receiver")
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
       

pre_save.connect(pets_pre_save_receiver, sender=Pet)