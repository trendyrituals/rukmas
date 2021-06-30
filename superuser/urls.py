from django.urls import path
from .views import home, add_product, products, view_all_bid, accept_bid, accepted_bids
urlpatterns = [
    path('pass_bid/',accepted_bids,name='all_accepted_bids'),
    path('bid_accept/<id>/<p_id>/', accept_bid, name='accpet_bid_url'),
    path('bid/<id>/',view_all_bid,name='product_bid_url'),
    path('products/',products,name='all_products'),
    path('add_product/', add_product, name='add_new_product'),
    path('', home, name='home_url')
]
