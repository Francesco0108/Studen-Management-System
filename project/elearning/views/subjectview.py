from django.shortcuts import redirect, render
from functools import wraps
from ..models import *
from ..forms import *
from django.contrib.auth.decorators import *
from django.conf import settings
from ..mydecorators import *
@staff_required
def subject_details(request,subject_id):
    all_status=SubjectStatus.objects.all()
    professor=Role.objects.get(name="Professor")
    student=Role.objects.get(name='Student')
    passed=SubjectStatus.objects.get(name='Polozen')
    enrolled=SubjectStatus.objects.get(name='Upisan')
    lost=SubjectStatus.objects.get(name='Izgubio/la pravo')
    try:
        sub=Predmeti.objects.get(id=subject_id)
    except:
        return render(request,'something_went_wrong.html')
    #print(sub)
    assistants=[]
    pass_student=[]
    enr_student=[]
    lost_student=[]
    try:
        enr=Enrollment.objects.filter(subject=sub).filter(usr__role=professor).values_list('usr')
    except:
        return render(request,'something_went_wrong.html')
    for i in enr:
        try:
            temp=Myuser.objects.get(id=i[0])
        except:
            return render(request,'something_went_wrong.html')
        assistants.append(temp)
    #print(assistants)
    try:
        enr1=Enrollment.objects.filter(subject=sub).filter(usr__role=student).filter(status=passed).values_list('usr')
    except:
        return render(request,'something_went_wrong.html')
    for i in enr1:
        try:
            temp=Myuser.objects.get(id=i[0])
        except:
            return render(request,'something_went_wrong.html')
        pass_student.append(temp)
    try:
        enr2=Enrollment.objects.filter(subject=sub).filter(usr__role=student).filter(status=enrolled).values_list('usr')
    except:
        return render(request,'something_went_wrong.html')
    for i in enr2:
        try:
            temp=Myuser.objects.get(id=i[0])
        except:
            return render(request,'something_went_wrong.html')
        enr_student.append(temp)
    try:
        enr3=Enrollment.objects.filter(subject=sub).filter(usr__role=student).filter(status=lost).values_list('usr')
    except:
        return render(request,'something_went_wrong.html')
    for i in enr3:
        try:
            temp=Myuser.objects.get(id=i[0])
        except:
            return render(request,'something_went_wrong.html')
        lost_student.append(temp)
    return render(request,'subject.html',{"sub":sub,"assistants":assistants,"pass_students":pass_student,"enr_students":enr_student,"lost_students":lost_student,"all_status":all_status})

@staff_required
def change_subject_status(request,subject_id,student_id,status_id):
    try:
        new_status=SubjectStatus.objects.get(id=status_id)
        subject=Predmeti.objects.get(id=subject_id)
        student=Myuser.objects.get(id=student_id)
        enr=Enrollment.objects.get(subject=subject,usr=student)
        enr.status=new_status
        enr.save()
    except:
        return render(request,'something_went_wrong.html')
    return redirect('http://localhost:8000/subject/'+str(subject_id))

@admin_required
def create_subject(request):
    try:
        prof_role=Role.objects.get(name="Professor")
        professors=Myuser.objects.filter(role=prof_role)
    except:
        return render(request,'something_went_wrong.html')
    if request.method=='GET':
        sub_form=SubjectForm(professors,request.POST or None)
        return render(request,'create_subject.html',{'form':sub_form})
    elif request.method=='POST':
        sub_form=SubjectForm(professors,request.POST)
        if sub_form.is_valid():
            try:
                sub_form.save()
            except:
                return render(request,'something_went_wrong.html')
            return redirect('home')

@admin_required
def update_subject(request,subject_id):
    try:
        prof_role=Role.objects.get(name="Professor")
        professors=Myuser.objects.filter(role=prof_role)
        subject=Predmeti.objects.get(id=subject_id)
    except:
        return render(request,'something_went_wrong.html')
    if request.method=='GET':
        update_form=SubjectForm(professors,instance=subject)
        return render(request,'create_subject.html',{'form':update_form})
    elif request.method=='POST':
        update_form=SubjectForm(professors,request.POST,instance=subject)
        if update_form.is_valid():
            try:
                update_form.save()
            except:
                return render(request,'something_went_wrong.html')
            return redirect('home')
@staff_required
def subject_users(request,subject_id):
    try:
        enr=Enrollment.objects.filter(subject__id=subject_id).values_list('usr')
        print(enr)
    except:
        return render(request,'something_went_wrong.html')
    users=[]
    for i in enr:
        try:
            tmp=Myuser.objects.get(id=i[0])
            users.append(tmp)
        except:
            return render(request,'something_went_wrong.html')
    print(users)
    return render(request,'users.html',{"users":users,"sub_id":subject_id})
@staff_required
def staff_unenroll(request,subject_id,user_id):
    try:
        print(subject_id)
        print(user_id)
        sub=Predmeti.objects.get(id=subject_id)
        usr1=Myuser.objects.get(id=user_id)
        enr=Enrollment.objects.get(subject=sub,usr=usr1)
        print(enr)
        enr.delete()
    except:
            return render(request,'something_went_wrong.html')
    return redirect('http://localhost:8000/users/'+str(subject_id))
@login_required
def unenroll(request,subject_id):
    try:
        enr=Enrollment.objects.get(usr__id=request.user.id,subject__id=subject_id)
    except:
        return render(request,'something_went_wrong.html')
    print(enr.status)
    #print(SubjectStatus.objects.get(id=enr.status))
    if(enr.status!=SubjectStatus.objects.get(name="Izgubio/la pravo")):
        try:
            enr.delete()
        except:
            return render(request,'something_went_wrong.html')
    return redirect('home')


def delete_subject(request,subject_id):
    try:
        sub=Predmeti.objects.get(id=subject_id)
        sub.delete()
    except:
            return render(request,'something_went_wrong.html')
    return redirect('home')
