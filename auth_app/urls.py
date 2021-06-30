from django.urls import path
from .views import login_view,sign_view,help_,check
urlpatterns = [
    path('check/',check,name='logout_help_url'),
    path('logout/',help_,name='logout_help_url'),
    path('login/', login_view, name='auth_login_url'),
    path('sign_up/', sign_view,name='auth_sign_up_url')
]
