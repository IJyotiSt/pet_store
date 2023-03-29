from django.views.generic import ListView,DetailView
from django.shortcuts import render,get_object_or_404
from django.http import Http404
from cart.models import Cart



from .models import Pet
 
# Create your views here.
class PetListView(ListView):
    queryset = Pet.objects.all()
    template_name = "petsapp/list.html"

#function based view
def pet_list_view(request):
    queryset = Pet.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "petsapp/list.html", context)



#class based view
class PetDetailView(DetailView):
    queryset = Pet.objects.all()
    print("default Manager",queryset)
    pet_data = Pet.pets.all()   
    print("custom Manager",pet_data)
    template_name = "petsapp/detail.html"
    def get_context_data(self, *args, **kwargs):
        context = super(PetDetailView, self).get_context_data(*args, **kwargs)
       # print(context)
        return context

def pet_detail_view(request, pk=None, *args, **kwargs):

    #instance = Pet.objects.get(pk=pk) #id
    # instance = get_object_or_404(Pet, pk=pk)
    #context = {
    #    'object': instance
    #}
    
    qs  = Pet.objects.filter(id=pk)	
    #print(qs)
    #print(Pet_data)
    if qs.exists() and qs.count() == 1: # len(qs)
        instance = qs.first()
    else:
        raise Http404("Pet doesn't exist")

    context = {
        'object': instance
    }
    return render(request, "petsapp/detail.html", context)



def pet_range_list_view(request):
    queryset = Pet.pets.get_pets_price_range(10000, 20000)
    context = {
        'object_list': queryset
    }
    return render(request, "petsapp/list.html", context)


class DogsListView(ListView):
    template_name = "petsapp/list.html"

    def get_queryset(self, *args, **kwargs):
        #request = self.request
        return Pet.pet.dog_list()

class CatsListView(ListView):
    template_name = "petsapp/list.html"

    def get_queryset(self, *args, **kwargs):
        #request = self.request
        return Pet.pet.cat_list()


class PetDetailSlugView(DetailView):
    print("=====")
    queryset = Pet.objects.all()
    model=Pet
    slug_field='slug'
    template_name = "Petsapp/detail.html"
   
    def get_object(self, *args, **kwargs):
        request = self.request
        print(request)
        slug = self.kwargs.get('slug')
        print("slug",slug)
        #instance = get_object_or_404(Pet, slug=slug, active=True)
        try:
            instance = Pet.objects.get(slug=slug)
            
            cartid=request.session.session_key
            incart= Cart.objects.filter(cart_id=cartid,pet=instance).exists()
            context={'incart':incart,'petobject':instance}
            print(incart,cartid)
            print(instance)
        except Pet.DoesNotExist:
            raise Http404("Not found..")
        except Pet.MultipleObjectsReturned:
            qs = Pet.objects.filter(slug=slug)
            instance = qs.first()
        except Exception as e:
           
            raise Http404("Errror ",e)
        
      
        return instance
    
