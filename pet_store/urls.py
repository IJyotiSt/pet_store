"""pet_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings

from django.conf.urls.static import static
from account.views import about_page,service_page,register_page,login_page,logOut
from petsapp.views import PetListView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('petsapp/', include('petsapp.urls',namespace='pets')),
    path('search/', include('search.urls',namespace='search')),
     path('cart/', include('cart.urls',namespace='cart')),
     path('orders/', include('orders.urls',namespace='orders')),
    path('', PetListView.as_view()),
     path('about/', about_page, name='aboutus'),
     path('service/', service_page, name='service'),
     path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logOut, name='logout'),
   

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


 #  path('', home_page, name='home'),
  # path('about/', about_page, name='about'),
  #  path('contact/$', contact_page, name='contact'),
  #  path('login/$', login_page, name='login'),
  # path('register/$', register_page, name='register'),