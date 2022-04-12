from django.urls import path
from . import views

urlpatterns = [
    path('Register',views.register,name='Register'),
    path('login',views.login,name='LOGIN'),
    path('logout',views.logout,name='LOGOUT')

]
