from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, DetailView, UpdateView
from .models import Employee

# Create your views here.
class Home(TemplateView):
    template_name = 'core/home.html'


class EmployeeListView(ListView):
    model = Employee
    template_name = "employee_list.html"


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = "employee_detail.html"


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = "employee_create_form.html"


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = "employee_update_form.html"


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = "employee_confirm_delete.html"
