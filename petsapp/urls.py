from django.urls import path
from petsapp import views

app_name = 'petsapp'
urlpatterns=[
    path('pets/', views.PetListView.as_view()),
    path('petlist/', views.pet_list_view,name='petlist'),
    path('rangelist/', views.pet_range_list_view),
    path('doglist/',views.DogsListView.as_view()),
    path('catlist/',views.CatsListView.as_view()),
    #path('<pk>/', views.PetDetailView.as_view()),
    path('<slug:slug>/', views.PetDetailSlugView.as_view(),name='detail'),
   # path('<pk>/', views.pet_detail_view ),
 ]
  