from django.urls import path 
from . import views



app_name="formapplication"

urlpatterns =[
    path('singup', views.singup , name="singup"),
    path('profile',views.profile , name='profile'),
    path('profile/edit', views.profile_edit , name="profile_edit")
]