from .base import *


def index (request):

    return HttpResponse("Hello ......")








class MyLeaveRequestsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated] # Only logged-in employees allowed

    serializer_class = LeaveRequestSerializer

    def get_queryset(self):
        # Only return leaves for the current user
        employee = Employee.objects.get(user_name=self.request.user)
        return LeaveRequest.objects.filter(employee=employee)

    def perform_create(self, serializer):
        # Assign the current employee automatically
        employee = Employee.objects.get(user_name=self.request.user)
        serializer.save(employee=employee, status='pending')



class LeaveRequestsView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    permission_classes = [IsHR]                        # Only HR can access
    serializer_class = LeaveRequestSerializer

    # ?employee_id=5&status=pending&leave_type=sick      sample
    def get_queryset(self):

        queryset = LeaveRequest.objects.all()

        employee_id = self.request.query_params.get('employee_id')
        status = self.request.query_params.get('status')
        leave_type = self.request.query_params.get('leave_type')
    
        if employee_id:         # Filter by employee id 
            queryset = queryset.filter(employee_id=employee_id)

        if status:         # Filter by leave status
            queryset = queryset.filter(status=status)

        if leave_type:        # Filter by leave type
            queryset = queryset.filter(leave_type=leave_type)
        
        return queryset






# taking id in url parms to get single leave request in update it's status
class LeaveRequestDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsHR]

    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer























