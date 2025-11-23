from rest_framework import serializers
from ..models.leave_request import LeaveRequest
from ..models.employee import Employee


from .employee import EmployeeSerializer




class LeaveRequestSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    
    class Meta:
        model = LeaveRequest
        fields = ['id', 'employee', 'leave_type', 'start_date', 'end_date', 'status']
        read_only_fields = ['employee', 'status']

    def validate(self, data):
        start = data.get('start_date')
        end = data.get('end_date')

        if end <= start:
            raise serializers.ValidationError({"end_date": "End date must be after start date."})

        # Get current employee
        employee = Employee.objects.get(user_name=self.context['request'].user)

        # Check overlapping leaves
        overlapping = LeaveRequest.objects.filter(
            employee=employee,
            status__in=['pending', 'approved'],
            start_date__lte=end,
            end_date__gte=start
        )

        if overlapping.exists():
            raise serializers.ValidationError(
                "There is already an overlapping leave request for these dates."
            )

        return data

    def create(self, validated_data):
        employee = Employee.objects.get(user_name=self.context['request'].user)
        validated_data['employee'] = employee
        validated_data['status'] = 'pending'
        return super().create(validated_data)
 