from django.urls import path
from. import views
urlpatterns = [
            path('loginUser/',views.loginUser,name='loginUser'),
            path('logout/',views.logoutpage,name='logout'),
            path('registerPage/',views.registerPage,name='registerPage'),
            path('getBlog/',views.getBlog,name='getBlog'),
            path('',views.home,name='home'),
    ]