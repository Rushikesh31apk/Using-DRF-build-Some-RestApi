from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company , Employee
from api.serializers import CompanySerializer , EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    # we have find employees of perticular company. end point: comapny/{company_id}/employees
    # http://127.0.0.1:8000/api/v1/companies/1/employees/
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            employees = Employee.objects.filter(company=company)
            # we have use serializer to convert data into json format
            serializer = EmployeeSerializer(employees, many=True, context={'request': request})
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)})




class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    



