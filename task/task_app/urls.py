from django.urls import path
from .import views

urlpatterns = [
    path('',views.Employee_add),
    path('Employee_list/',views.Employee_list, name='Employee_list'),
    path('employee/<int:id>/', views.employee_detail, name='employee_detail'),
    path('api/employees/', views.get_employees),
    path('api/employees/create/', views.create_employee),
    path('employee/edit/<int:id>/', views.employee_edit, name='employee_edit'),
    path('employee/delete/<int:id>/', views.employee_delete, name='employee_delete'),
    
]