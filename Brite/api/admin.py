from django.contrib import admin
from .models import Company, Employee, LeaveRequest

# Optional: Customize the list display for better readability
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'major')
    search_fields = ('name', 'location', 'major')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'company', 'role', 'joining_date', 'user_name')
    search_fields = ('name', 'email')
    list_filter = ('role', 'company')


@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'leave_type', 'start_date', 'end_date', 'status')
    list_filter = ('status', 'leave_type')
    search_fields = ('employee__name', 'employee__email')
