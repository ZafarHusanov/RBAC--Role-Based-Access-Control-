from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

from . import models
from .decorators import has_permission

@has_permission('retrive_job')
def job_list(request):
    data = models.Module.objects.all()
    return HttpResponse(data)

@has_permission('update_project')
def project_edit(request):
    # ...
    pass

@csrf_exempt
def log_in(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse('Log In System')
    else:
        return HttpResponse('Notogri usename yoki password.')

