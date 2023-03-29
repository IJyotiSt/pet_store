from django.urls import path
from. views import cart_home,add_to_card,update_cart,delete_cart
        
app_name="cart"
urlpatterns = [
    path('cartpage/',cart_home,name='cartpage'),
    path('addtocart/<int:id>',add_to_card,name='addtocart'),
    path('updatecart/',update_cart,name='updatecart'),
    path('deleteitem/<int:id>',delete_cart,name='deleteitem'),
    ]