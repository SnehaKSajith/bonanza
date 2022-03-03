from django.urls import path
from .import views

urlpatterns=[

    path('',views.home, name="home"),
    path('signup',views.signup, name="sign"),
    path('login',views.login, name="login"),
    path('usermaster',views.usermaster, name="usermaster"),
    path('myprofile',views.myprofile, name="myprofile"),
    path('springwhites',views.springwhites, name="springwhites"),
    
]