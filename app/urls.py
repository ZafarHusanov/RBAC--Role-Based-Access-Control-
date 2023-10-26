from django.urls import path
from . import views


urlpatterns = [
    path('job-list/', views.job_list),
    path('login/', views.log_in),
]