from .models import Tag

qs = Tag.objects.all()
print(qs)
 from .models import Tag
Traceback (most recent call last):
  File "<console>", line 1, in <module>
>>> qs = Tag.objects.all()
>>> qs
<QuerySet [<Tag: Brown>, <Tag: white>]>
>>> white=Tag.objects.last()
>>> white.name
'white'
>>> white.pet
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Tag' object has no attribute 'pet'
>>> white.pets
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x000001BFF521D7D0>
>>> white.pets.all()
<QuerySet [<Pet: Pet object (4)>, <Pet: Pet object (5)>, <Pet: Pet object (6)>, <Pet: Pet object (7)>]>
>>> exit()

#==============================
>>> from petsapp.models import Pet
>>> qs=Pet.object.all()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: type object 'Pet' has no attribute 'object'
>>> qs=Pet.objects.all()
>>> qs
<QuerySet [<Pet: Pet object (1)>, <Pet: Pet object (2)>, <Pet: Pet object (3)>, <Pet: Pet object (4)>, <Pet: Pet object (5)>, <Pet: Pet object (6)>, <Pet: Pet object (7)>]>
>>> pet=qs.first()
>>> pet
<Pet: Pet object (1)>
>>> pet.name
'rockey'
>>> pet.description
'cheerful'
>>> pet.tag
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Pet' object has no attribute 'tag'
>>> pet.tag_set
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x0000024628653B90>
>>> pet.tag_set.all()
<QuerySet [<Tag: Brown>, <Tag: age_above_5>]>