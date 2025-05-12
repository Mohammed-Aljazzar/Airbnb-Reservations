from django.urls import path
from . import views
# from .views import 

app_name = 'about'

urlpatterns = [
    path('', views.AboutView.as_view(), name='about'),
   
]
