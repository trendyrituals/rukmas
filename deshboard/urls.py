from django.urls import path
from .views import desh
urlpatterns = [
    path('', desh, name='desh_landing_url')
]
