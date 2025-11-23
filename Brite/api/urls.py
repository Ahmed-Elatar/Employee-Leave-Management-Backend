from django.urls import path 

from .views.authenticate import SignupAPIView , LoginAPIView , user_logout
from .views.leaves_requests import index ,  MyLeaveRequestsView , LeaveRequestsView, LeaveRequestDetailView 
from .views.companies import *


urlpatterns = [
    

    path('',index , name= 'index'),
    path('singup/',SignupAPIView.as_view() , name= 'user_singup'),
    path('login/',LoginAPIView.as_view() , name= 'user_login' ), 
    path('logout/', user_logout , name='user_logout'),

    
    path('leaves/', LeaveRequestsView.as_view(), name= 'leave_requests'),        #List all leaves requests - only retrive - need hr permission      
    path('my-leave-requests/',MyLeaveRequestsView.as_view(), name= 'my_leave_request'), # List all leaves requests for logged in user - List and create       
    path('leave-requests/<int:pk>/', LeaveRequestDetailView.as_view(), name= 'single_leave_request'),  #List single leave request - retrive and update to change status- need hr permission
    
    path('companies/',CompaniesView.as_view(), name= 'compaies'),
]
