from django.db import models

# Create your models here.

# creating compony model
class Company(models.Model):
    company_id= models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    company_email = models.EmailField(max_length=100)
    company_phone = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100)
    company_description = models.TextField(max_length=1000)
    company_status = models.BooleanField(default=True)
    type = models.CharField(max_length= 100, choices= (
        ('IT','IT'),
        ( 'Finace', 'Finace'),
        ( 'Educational','Educational'),
        ( 'Hardware','Hardware')
        ), default='IT'
    )
    added_date = models.DateTimeField(auto_now_add=True)

# Employee Model
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=100)
    employee_email = models.EmailField(max_length=100)
    employee_phone = models.CharField(max_length=10)
    employee_address = models.CharField(max_length=100)
    position = models.CharField(
    max_length=100,
    choices=(
        ('Software Developer', 'Software Developer'),
        ('Network Engineer', 'Network Engineer'),
        ('IT Support Specialist', 'IT Support Specialist'),
        ('System Administrator', 'System Administrator'),
        ('Database Administrator', 'Database Administrator'),

        ('Chief Financial Officer (CFO)', 'Chief Financial Officer (CFO)'),
        ('Finance Manager', 'Finance Manager'),
        ('Accountant', 'Accountant'),
        ('Financial Analyst', 'Financial Analyst'),
        ('Auditor', 'Auditor'),
        
        ('Healthcare Administrator', 'Healthcare Administrator'),
        ('Nurse', 'Nurse'),
        ('Physician', 'Physician'),
        ('Medical Assistant', 'Medical Assistant'),
        ('Lab Technician', 'Lab Technician'),
        
        ('Teacher', 'Teacher'),
        ('Principal', 'Principal'),
        ('Counselor', 'Counselor'),
        ('Educational Coordinator', 'Educational Coordinator'),
        
        ('Hardware Engineer', 'Hardware Engineer'),
        ('Hardware Technician', 'Hardware Technician'),
        ('Product Designer', 'Product Designer'),
        ('Field Service Engineer', 'Field Service Engineer'),
     ),
        default='Software Developer'
    )
    employee_status = models.BooleanField(default=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    