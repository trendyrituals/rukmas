from django.urls import path
from .views import product_list,product_view
urlpatterns = [
    path('product_view/<id>',product_view,name='product_view_url'),
    path('', product_list, name='landing_url')
]
