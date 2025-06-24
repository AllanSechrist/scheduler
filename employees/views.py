from django.shortcuts import render
from django.views.generic import ListView
from .models import Employee

# Create your views here.
class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee/employee_list.html'
    context_object_name = 'employees'

class EmployeeDetailView(ListView):
    model = Employee
    template_name = 'employee/employee_detail.html'
    context_object_name = 'employee' 
    