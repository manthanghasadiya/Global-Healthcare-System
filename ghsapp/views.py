from django.shortcuts import render, redirect
from .models import userInfo, doctorInfo, History, Appointment, Feedback
from .forms import userForm, userInfoForm, doctorInfoForm
from .filters import doctor_filter
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'home.html')

def test(request):
    return render(request, 'test.html')


def index(request):
    if request.method == 'POST':
        user_form = userForm(request.POST)
        user_info_form = doctorInfoForm(request.POST, request.FILES)

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_info = user_info_form.save(commit=False)
            user_info.doctor = user
            user_info.save()

            # login(request, user)

            return redirect('home')

        else:
            context = {
                'user_form.errors': user_form.errors, 'user_info_form.errors': user_info_form.errors,
                'user_form': user_form, 'user_info_form': user_info_form
            }
            return render(request, 'index.html', context)

    else:
        user_form = userForm()
        user_info_form = doctorInfoForm()

        context = {'user_form': user_form, 'user_info_form': user_info_form}
        return render(request, 'index.html', context)


    # return render(request, 'index.html')


def ohome(request):
    return render(request, 'originalhome.html')

def s(request):
    return render(request,'book.html')

def signup_doctor(request):
    if request.method == 'POST':
        user_form = userForm(request.POST)
        user_info_form = doctorInfoForm(request.POST, request.FILES)

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_info = user_info_form.save(commit=False)
            user_info.doctor = user
            user_info.save()
            
            login(request, user)

            return redirect('doctor_home')

        else:

            context = {
                'user_form.errors': user_form.errors, 'user_info_form.errors': user_info_form.errors,
                'user_form': user_form, 'user_info_form': user_info_form
            }
            return render(request, 'signup_doctor.html', context)

    else:
        user_form = userForm()
        user_info_form = doctorInfoForm()

        context = {'user_form': user_form, 'user_info_form': user_info_form}
        return render(request, 'signup_doctor.html', context)


def signup_user(request):

    if request.method == 'POST':
        user_form = userForm(request.POST)
        user_info_form = userInfoForm(request.POST, request.FILES)

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_info = user_info_form.save(commit=False)
            user_info.user = user
            user_info.save()

            login(request, user)

            return redirect('user_home')

        else:

            context = {
                'user_form.errors': user_form.errors, 'user_info_form.errors': user_info_form.errors,
                'user_form': user_form, 'user_info_form': user_info_form
            }
            return render(request, 'signup_user.html', context)

    else:
        user_form = userForm()
        user_info_form = userInfoForm()

        context = {'user_form': user_form, 'user_info_form': user_info_form}
        return render(request, 'signup_user.html', context)


def signin(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)

            try:
                doctorInfo.objects.get(doctor=request.user)
                return redirect('doctor_home')

            except:
                return redirect('user_home')

        else:
            return redirect('signin')

    else:
        return render(request, 'user/signin.html')


@login_required(login_url='error')
def signout(request):
    logout(request)
    return redirect('home')


def error(request):
    return render(request, 'error.html')


@login_required(login_url='error')
def user_home(request):
    user = userInfo.objects.get(user=request.user)

    context = {
        'user':user
    }
    
    return render(request, 'user_home.html', context)


@login_required(login_url='error')
def doctor_home(request):
    user = doctorInfo.objects.get(doctor=request.user)

    context = {
        'user': user
    }

    return render(request, 'doctor_home.html', context)


@login_required(login_url='error')
def history(request):

    users = History.objects.filter(user=request.user)

    context = {
        'users': users
    }

    try:
        doctorInfo.objects.get(doctor=request.user)
        return render(request, 'user/history.html', context)
    except:
        return render(request, 'history_user.html', context)


@login_required(login_url='error')
def patient_history(request, pk):

    users = History.objects.filter(user=pk)

    context = {
        'users':users
    }

    return render(request, 'patient_history.html', context)


@login_required(login_url='error')
def book_appointment(request):

    # bikes = Bike.objects.filter(bike_available="Available")
    # bikes_filter = bike_filter(request.GET, queryset=bikes)
    # context = {'bikes': bikes, 'filter': bikes_filter}
    doctors = doctorInfo.objects.all()
    doctor_fil = doctor_filter(request.GET, queryset=doctors)

    context = {
        'filter': doctor_fil
    }

    if request.method == 'POST':
        doctor = request.POST.get('doctor')
        date = request.POST.get('date')
        time = request.POST.get('time')

        dc = User.objects.get(id=doctor)

        form = Appointment()

        form.user_app = request.user
        form.doctor_app = dc
        form.date = date
        form.time = time

        form.save()

    try:
        doctorInfo.objects.get(doctor=request.user)
        return render(request, 'user/book_appointment.html', context)
    except:
        return render(request, 'book_appointment_user.html', context)

    return render(request, 'user/book_appointment.html', context)



@login_required(login_url='error')
def show_appointment(request):
    appointments = Appointment.objects.filter(user_app=request.user)
    
    context = {
        'appointments': appointments
    }

    try:
        doctorInfo.objects.get(doctor=request.user)
        return render(request, 'user/show_appointment.html', context)
    except:
        return render(request, 'show_appointment_user.html', context)


@login_required(login_url='error')
def doctor_show_appointment(request):
    appointments = Appointment.objects.filter(doctor_app=request.user)
    
    context = {
        'appointments': appointments
    }

    return render(request, 'doctor/show_appointment.html', context)


@login_required(login_url='error')
def check_patient(request, pk):
    
    appointment = Appointment.objects.get(id=pk)

    context = {
        'appointment': appointment
    }

    if request.method == 'POST':

        disease = request.POST.get('disease')
        medicine = request.POST.get('medicine')
        charges = request.POST.get('charges')
        hospital_name = request.POST.get('hospital_name')
        
        app = History()

        us = appointment.user_app

        app.doctor = request.user
        app.user = us 
        app.disease = disease
        app.medicine = medicine
        app.charges = charges
        app.hospital_name = hospital_name

        app.save()
        
        appointment.delete()

        return redirect('doctor_home')

    return render(request, 'checkup.html', context)


@login_required(login_url='error')
def feedback(request):

    doctors = doctorInfo.objects.all()

    context = {
        'doctors': doctors
    }

    if request.method == 'POST':
        doctor = request.POST.get('doctor')
        waiting_time = request.POST.get('waiting_time')
        recommendation = request.POST.get('recommendation')
        feedback = request.POST.get('feedback')

        fdbck = Feedback()

        
        dc = User.objects.get(id=doctor)

        fdbck.user_feed = request.user
        fdbck.doctor_feed = dc
        fdbck.waiting_time = waiting_time
        fdbck.recommendation = recommendation
        fdbck.feedback = feedback

        fdbck.save()

        return redirect('user_home')

    return render(request, 'feedback.html', context)
