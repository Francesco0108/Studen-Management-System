from django.shortcuts import redirect, render
from ..models import *
from django.contrib.auth.hashers import make_password
from ..mydecorators import *
@login_required
def home(request):
    try:
        admin=Role.objects.get(name='Admin')
        s=Status.objects.get(name='Redovni')
        subjects=None
        r=Role.objects.get(name='Admin')

        r1=Role.objects.get(name='Professor')
        final=None
    except:
        return render(request,'something_went_wrong.html')
    if(request.user.role==r):
        try:
            final=Predmeti.objects.all()
        except:
            return render(request,'something_went_wrong.html')
    elif request.user.role==r1:
        try:
            subjects=Predmeti.objects.filter(nositelj=request.user)
            enr=Enrollment.objects.filter(usr=request.user).values_list('subject')
        except:
            return render(request,'something_went_wrong.html')
        res_list = [x[0] for x in enr]
        try:
            sub2=Predmeti.objects.filter(pk__in=enr)
            final=subjects | sub2
        except:
            return render(request,'something_went_wrong.html')
    else:
        try:
            enr=Enrollment.objects.filter(usr=request.user).values_list('subject')
        except:
            return render(request,'something_went_wrong.html')
        res_list = [x[0] for x in enr]
        try:
            sub2=Predmeti.objects.filter(pk__in=enr)
        except:
            return render(request,'something_went_wrong.html')
        final=sub2
    #print(subjects)
    #print(request.user.role)
    return render(request,'home.html',{"data":final})


def root(request):
    return redirect('login')
    