from django.urls import path
from .views import entry_bid
urlpatterns = [
    path('<product_id>/', entry_bid, name='entry_bid_url')
]
