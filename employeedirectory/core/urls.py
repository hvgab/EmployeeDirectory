
from django.urls import path
from .views import Home
from .views import EmployeeCreateView, EmployeeDeleteView, EmployeeDetailView, EmployeeListView, EmployeeUpdateView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('employees', EmployeeListView.as_view(), name='employee-list'),
    path('employees/create', EmployeeCreateView.as_view(), name='employee-create'),
    path('employees/<id>', EmployeeDetailView.as_view(), name='employee-list'),
    path('employees/<id>/update', EmployeeUpdateView.as_view(), name='employee-update'),
    path('employees/<id>/delete', EmployeeDeleteView.as_view(), name='employee-delete'),
]
 