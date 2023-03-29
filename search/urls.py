from django.urls import path

from .views import DogsListView,CatsListView,SearchPetView,SearchQueryView
        
app_name="search"
urlpatterns = [
    path('dog_list/', DogsListView.as_view(), name='Doglist'),
    path('cat_list/', CatsListView.as_view(), name='Catlist'),
    path('searchqview/', SearchQueryView.as_view(),name="q"),
    path('searchview/', SearchPetView.as_view(),name="query"),
]