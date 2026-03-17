from django.shortcuts import render,redirect
from .models import Employee, Department
from django.db.models import Q
from django.http import JsonResponse
import json




def Employee_add(request):

    departments = Department.objects.all()

    if request.method == 'POST':

        name           = request.POST.get('name')
        role           = request.POST.get('role')
        department_id  = request.POST.get('department')
        email          = request.POST.get('email')

        department_obj = Department.objects.get(id=department_id)

        Employee.objects.create(
            name       = name,
            Role       = role,
            department = department_obj,
            Email      = email,
        )

        return redirect('Employee_list')

    return render(request, 'add_employe.html', {'departments': departments})


def Employee_list(request):
    search      = request.GET.get('search')

    if search:
        employee = Employee.objects.filter(
            Q(name__icontains=search) |
            Q(department__name__icontains=search)
        )
    else:
        employee = Employee.objects.all()

    return render(request, 'employe_view.html', {'employee': employee})


def employee_detail(request, id):
    emp = Employee.objects.get(id=id)

    return render(request, 'employee_detail.html', {'emp': emp})



def get_employees(request):
    employees = Employee.objects.all()

    data = []
    for emp in employees:
        data.append({
            'id': emp.id,
            'name': emp.name,
            'role': emp.Role,
            'department': emp.department.name,
            'email': emp.Email
        })

    return JsonResponse(data, safe=False)



def create_employee(request):
    if request.method == "POST":
        data          = json.loads(request.body)

        name          = data.get('name')
        role          = data.get('role')
        department_id = data.get('department')
        email         = data.get('email')

        department = Department.objects.get(id=department_id)

        emp = Employee.objects.create(
            name       = name,
            Role       = role,
            department = department,
            Email      = email
        )

        return JsonResponse({'message': 'Employee created', 'id': emp.id})



def employee_edit(request, id):
    emp                = Employee.objects.get(id=id)
    departments        = Department.objects.all()

    if request.method == 'POST':
        emp.name       = request.POST.get('name')
        emp.Role       = request.POST.get('role')
        emp.Email      = request.POST.get('email')

        dept_id        = request.POST.get('department')
        emp.department = Department.objects.get(id=dept_id)

        emp.save()
        return redirect('Employee_list')

    return render(request, 'edit_employee.html', {
        'emp': emp,
        'departments': departments
    })



def employee_delete(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect('Employee_list')





