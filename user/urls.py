from django.urls import *
from .views import *

urlpatterns=[
    path ("register/",userRegister,name='register'),
    path("login",userLogin,name="login"),
    path("profiles/",profiles,name="profiles"),
    path("olustur/" ,olustur, name="olustur"),
    path('hesap/', hesap , name='hesap'),
    path('delete/',sil ,name='delete'),
    path('update/' , update, name='update'),
    path('logout/',userLogout , name='logout')
]