from django.urls import path
# from .views import profile , profile_edit , signup 
from .views import profile , profile_edit , signup , myreservation ,mylisting, add_feedback, custom_logout


app_name = 'accounts'

urlpatterns = [
    path('signup',signup , name='signup'),
    path('profile/',profile,name='profile'),
    path('profile/edit', profile_edit , name='profile_edit') ,
    path('reservation/', myreservation , name='myreservation') ,
    path('mylisting/', mylisting , name='mylisting') ,
    path('profile/booking/<slug:slug>/review', add_feedback , name='add_feedback'),
    path('logout/', custom_logout , name='logout'),
]
