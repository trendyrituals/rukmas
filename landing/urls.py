from django.urls import path
from .views import home, about
urlpatterns = [
    path('about/',about,name='about_url'),
    path('', home, name='landing_url')
]
