
from django.shortcuts import redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout,get_user


from ..forms.authenticate import *

from ..models.employee import Employee
from ..models.company import Company
from ..models.leave_request import LeaveRequest

from ..serializers.leave_request import LeaveRequestSerializer
from ..serializers.employee import CompanySerializer , EmployeeSerializer

from ..permissions.hr_permissions import IsHR


from rest_framework import generics

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated

