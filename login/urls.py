from django.contrib import admin
from django.urls import path,include
from login import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('details/',views.all_details),
    path('users/',views.all_users),
    path('<str:username>',views.user_details),
    path('',views.home),
    path('login/',views.login, name='login'),
    path('signup/',views.signup, name='signup'),
]