from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, logout, login

# Renders the 'about.html' page
def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')

    doctors = Doctor.objects.all()  # Retrieve all doctor objects
    patient = Patient.objects.all()
    appointment = Appointment.objects.all()

    d = 0
    p = 0
    a = 0

    # Count the number of doctors
    for i in doctors:
        d += 1
    for i in patient:
        p += 1
    for i in appointment:
        a += 1

    d1 = {'d': d, 'p': p, 'a': a}  # Data dictionary to pass to the template
    return render(request, 'index.html', d1)

# Handles user login and renders the 'login.html' page
def Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']  # Retrieve username from POST data
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)  # Authenticate the user
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"

    d = {'error': error}  # Data dictionary to pass to the template
    return render(request, 'login.html', d)

# Logs out the user and redirects to the login page
def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

# Renders the 'view_doctor.html' page with all doctors
def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()  # Retrieve all doctor objects
    d = {'doc': doc}  # Data dictionary to pass to the template
    return render(request, 'view_doctor.html', d)

# Handles the addition of a new doctor and renders the 'add_doctor.html' page
def Add_Doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    if request.method == 'POST':
        name = request.POST.get('name')  # Retrieve doctor's name from POST data
        contact = request.POST.get('contact')
        special = request.POST.get('special')

        try:
            Doctor.objects.create(name=name, contact=contact, special=special)  # Create a new doctor
            error = "no"
        except Exception as e:
            print(f"Error: {e}")
            error = "yes"

    return render(request, 'add_doctor.html', {'error': error})

# Handles the deletion of a doctor and redirects to the 'view_doctor' page
def Delete_Doctor(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=pid)  # Retrieve doctor by ID
    doctor.delete()
    return redirect('view_doctor')


def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.all()
    d = {'pat': pat}
    return render(request, 'view_patient.html', d)


def Add_Patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        g = request.POST['gender']
        c = request.POST['contact']
        a = request.POST['address']
        try:
            Patient.objects.create(name=n, gender=g, contact=c, address=a)
            error = "no"

        except:
            error = "yes"

    d = {'error': error}

    return render(request, 'add_patient.html', d)


def Delete_Patient(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')


def View_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    appoint = Appointment.objects.all()
    d = {'appoint': appoint}
    return render(request, 'view_appointment.html', d)


def Add_Appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()

    if request.method == 'POST':
        d_id = request.POST['doctor']
        p_id = request.POST['patient']
        d1 = request.POST['date']
        t = request.POST['time']

        try:
            doctor = Doctor.objects.get(id=d_id)
            patient = Patient.objects.get(id=p_id)
            Appointment.objects.create(doctor=doctor, patient=patient, date1=d1, time1=t)
            error = "no"
        except Exception as e:
            print(f"Error: {e}")
            error = "yes"

    d = {'doctor': doctor1, 'patient': patient1, 'error': error}

    return render(request, 'add_appointment.html', d)


def Delete_Appointment(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    appointment = Appointment.objects.get(id=pid)
    appointment.delete()
    return redirect('view_appointment')
