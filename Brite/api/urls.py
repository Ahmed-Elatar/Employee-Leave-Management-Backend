from django.urls import path 
from .views import *
urlpatterns = [
    
    path('singin/',SignupAPIView.as_view()),
    path('login/',LoginAPIView.as_view()),
    path('companies/',CompaniesView.as_view()),

]
