from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ohome', views.ohome, name='ohome'),
    path('signup_user/', views.signup_user, name='signup_user'),
    path('signup_doctor', views.signup_doctor, name='signup_doctor'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('error', views.error, name='error'),
    path('user_home', views.user_home, name='user_home'), 
    path('doctor_home', views.doctor_home, name='doctor_home'),
    path('index', views.index, name='index'),
    path('s',views.s,name='s'),
    path('history', views.history, name='history'),
    path('book_appointment', views.book_appointment, name='book_appointment'),
    path('show_appointment', views.show_appointment, name='show_appointment'),
    path('doctor_show_appointment', views.doctor_show_appointment, name='doctor_show_appointment'),
    path('check_patient/<str:pk>/', views.check_patient, name='check_patient'),
    path('patient_history/<str:pk>/', views.patient_history, name='patient_history'),
    path('test', views.test, name='test' ),
    path('feedback', views.feedback, name='feedback'),
]
