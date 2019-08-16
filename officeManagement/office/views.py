from django.shortcuts import render,redirect
from .forms import StaffForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .models import Department, Staff
from django.contrib.auth.models import User
import random
import datetime
# Create your views here.
def createuser(request):
    user = request.user
    form = StaffForm()
    if request.method == "POST":
        form = StaffForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data.get('first_name')
            lastname = form.cleaned_data.get('last_name')
            name = firstname + " " + lastname 
            age = form.cleaned_data.get('age')
            department = form.cleaned_data.get('department')
            address = form.cleaned_data.get('address')
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            user = form.save()
            pw = user.password
            user.set_password(pw)
            user.save()

            departments = Department.objects.get(name = department)
            user_detail =  User.objects.get(username = username)
            staff = Staff(name = name , age = age , email = email, address = address, staff_id = random.randint(1, 1000) , department = departments, user = user_detail )
            staff.save()
            messages.success(request, "Staff Created Successfully")
    else:
        form = StaffForm()
    context = {'form' : form}
    return render(request,"office/signup.html", context)

def init_login(request):
    return render(request,"office/login.html")

def login_view(request):
    username = request.POST.get("username", None)
    password = request.POST.get("password", None)
    login_user = authenticate(request, username=username, password=password)
    if login_user is not None:
        login(request, login_user)
        return redirect("office:user_details")
    else:
        messages.error(request, "Invalid Login Credentials")
        return redirect("office:init_login")
    

def logout_view(request):
    logout(request)
    return redirect("office:init_login")

def user_details(request):
    if request.user.is_authenticated:
        user = request.user
        user_id = request.user.id
        staff = Staff.objects.get(user = user_id)
    else:
        messages.error(request, "Please Login First")
        return redirect("office:init_login")
    
    context = {"user": user, "staff" : staff }

    return render(request, "office/user_details.html", context )

def status(request):
    user = request.user
    if user.is_authenticated:
        user_id = request.user.id
        staff = Staff.objects.get(user = user_id)
        resumption_date = staff.resumption_date
        print(resumption_date)
        six_months_time = resumption_date + datetime.timedelta(6*365/12)
        print(six_months_time)
        print(datetime.date.today())
        if datetime.date.today() >= resumption_date + datetime.timedelta(6*365/12):
            staff.status = "Yes"
            staff.save()
            print("Due for leave")
        else:
            print("not due for leave")
    else:
        messages.error(request, "Please Login First")
        return redirect("office:init_login")
    context = {"user":user, "staff": staff, "date": six_months_time}
    return render(request, "office/status.html", context)


def change_details(request):
    user = request.user
    if user.is_authenticated:
        user_id = request.user.id
        staff = Staff.objects.get(user = user_id)
        context = {"user": user, "staff":staff}
        return render(request,"office/change_details.html",context)
    else:
        messages.error(request, "Please Login First")
        return redirect("office:init_login")


def init_details(request):
    user = request.user
    if user.is_authenticated:
        user_id = request.user.id
        staff = Staff.objects.get(user = user_id)
        name = request.POST.get("name", None)
        age = request.POST.get("age", None)
        address = request.POST.get("address", None)
        email = request.POST.get("email", None)
        staff.name = name
        staff.age = age
        staff.address = address
        staff.email = email
        staff.save()
        return redirect("office:my_info")

    else:
        messages.error(request, "Please Login First")
        return redirect("office:init_login")
    context = {"user": user, "staff":staff}

def my_info(request):
    user = request.user
    if user.is_authenticated:
        user_id = request.user.id
        staff = Staff.objects.get(user = user_id)
        context = {"user" : user, "staff": staff}
        return render(request, "office/my_info.html", context)
    else:
        messages.error(request, "Please Login First")
        return redirect("office:init_login")

def all_staff(request):
    user = request.user
    staffs = Staff.objects.all()
    context = {"user" : user , "staffs": staffs}
    return render(request, "office/all_staff.html", context)