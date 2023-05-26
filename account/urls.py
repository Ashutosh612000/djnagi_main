from django.urls import path
from account.views import handleSignup,index,handlelogin,showusers,handlelogout,delete_data,update_data

urlpatterns = [

    path('',index,name='index'),
    path('signup/',handleSignup,name='handleSignup'),
    path('login/',handlelogin,name='handlelogin'),
    path('showusers/',showusers,name='showusers'),
    path('logout/',handlelogout,name='handlelogout'),

    path('delete/<int:id>/',delete_data,name="deletedata"),
    path('<int:id>/',update_data,name='updatedata'),
]
