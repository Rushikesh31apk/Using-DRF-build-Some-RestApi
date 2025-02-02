from rest_framework import serializers
from .models import Company, Employee

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

''' HyperlinkedModelSerializer                   ModelSerializer 
1) Uses hyperlinks                               1) Uses primary keys  
2) url field Automatically included              2) url field Not included by default
3) Navigation More API-friendly                  3) Less intuitive
'''
'''
Key Features:
1) Hyperlinked relationships – Instead of using an id field, related objects are represented by their URLs.
2) Requires a view_name – It uses Django’s reverse URL resolution to generate URLs for related objects.
3) Typically used with HyperlinkedIdentityField and HyperlinkedRelatedField to create links
'''
