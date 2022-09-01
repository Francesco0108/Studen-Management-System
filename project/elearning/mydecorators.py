from django.shortcuts import redirect, render
from functools import wraps
from .models import *
from .forms import *
from django.contrib.auth.decorators import *
from django.conf import settings
def admin_required(function):
    def wrapper(request,*args,**kwargs):
        if(request.user.role.name!='Admin'):
            return render(request,'forbidden.html')
        else:
            return function(request,*args,**kwargs)
    return wrapper
def staff_required(function):
    def wrapper(request,*args,**kwargs):
        if(request.user and (request.user.role.name=='Admin' or request.user.role.name=='Professor')):
            return function(request,*args,**kwargs)
        else:
            return render(request,'forbidden.html')
    return wrapper