from .base import *






#  Companies View 
class CompaniesView(generics.ListCreateAPIView):
    permission_classes = [IsHR]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


