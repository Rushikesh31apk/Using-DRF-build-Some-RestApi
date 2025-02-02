# Generated by Django 5.1.5 on 2025-02-02 06:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_name', models.CharField(max_length=100)),
                ('employee_email', models.EmailField(max_length=100)),
                ('employee_phone', models.CharField(max_length=10)),
                ('employee_address', models.CharField(max_length=100)),
                ('position', models.CharField(choices=[('Software Developer', 'Software Developer'), ('Network Engineer', 'Network Engineer'), ('IT Support Specialist', 'IT Support Specialist'), ('System Administrator', 'System Administrator'), ('Database Administrator', 'Database Administrator'), ('Chief Financial Officer (CFO)', 'Chief Financial Officer (CFO)'), ('Finance Manager', 'Finance Manager'), ('Accountant', 'Accountant'), ('Financial Analyst', 'Financial Analyst'), ('Auditor', 'Auditor'), ('Healthcare Administrator', 'Healthcare Administrator'), ('Nurse', 'Nurse'), ('Physician', 'Physician'), ('Medical Assistant', 'Medical Assistant'), ('Lab Technician', 'Lab Technician'), ('Teacher', 'Teacher'), ('Principal', 'Principal'), ('Counselor', 'Counselor'), ('Educational Coordinator', 'Educational Coordinator'), ('Hardware Engineer', 'Hardware Engineer'), ('Hardware Technician', 'Hardware Technician'), ('Product Designer', 'Product Designer'), ('Field Service Engineer', 'Field Service Engineer')], default='Software Developer', max_length=100)),
                ('employee_status', models.BooleanField(default=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
        ),
    ]
