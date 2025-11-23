from rest_framework.permissions import BasePermission
from ..models import Employee

class IsHR(BasePermission):
    """
    Allows access only to employees with role = 'hr'.
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        try:
            employee = Employee.objects.get(user_name=request.user)
        except Employee.DoesNotExist:
            return False
        
        return employee.role == 'hr'