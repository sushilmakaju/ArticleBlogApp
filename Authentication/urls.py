from django.urls import path
from .views import *
urlpatterns = [
    path('register/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout')
]
