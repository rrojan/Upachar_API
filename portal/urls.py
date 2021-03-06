from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *


app_name='portal'

urlpatterns = [
    path('', index_view, name='dashboard'),
    path('today/', reports_today_view, name='reports_today'),
    path('archive/', reports_archive_view, name='archive'),

    path('all_patients/', all_patients_view, name='all_patients'),
    path('all_patients/<int:pk>', patient_detail_view, name='patient_detail'),
    path('add_patient/', patient_add_view, name='patient_add'),

    path('assign/', assign_view, name='assign'),
    path('assign/<int:pk>/', assign_patient_view, name='assign_patient'),

    path('all_doctors/', all_doctors_view, name='all_doctors'),
    path('all_doctors/<int:pk>/', doctor_detail_view, name='doctor_detail'),
    path('add_doctor/', doctor_add_view, name='doctor_add'),
    
    path('reports/<int:pk>/', report_detail_view, name='report_detail'),

    path('login/', LoginView.as_view(template_name="portal/login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="portal/logout.html"), name='logout'),
]