from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password

from elearning.forms.enrollform import EnrollForm
from elearning.mydecorators import admin_required, staff_required
from ..models import *
from ..forms import *
@admin_required
def create_user(request):
    if request.method=='GET':
        user_form=UserForm()
        return render(request,'create_user.html',{'form':user_form})
    elif request.method=='POST':
        user_form=UserForm(request.POST)
        #print(user_form.cleaned_data())
        if user_form.is_valid():
            try:
                username=user_form.cleaned_data['username']
                password=make_password(user_form.cleaned_data['username'])
                firstname=user_form.cleaned_data['first_name']
                lastname=user_form.cleaned_data['last_name']
                email=user_form.cleaned_data['email']
                role=user_form.cleaned_data['role']
                status=user_form.cleaned_data['status']
                superuser=user_form.cleaned_data['is_superuser']
                staff=user_form.cleaned_data['is_staff']
                user=Myuser(username=username,password=password,first_name=firstname,last_name=lastname,email=email,role=role,status=status,is_superuser=superuser,is_staff=staff)
                user.save()
            except:
                return render(request,'something_went_wrong.html')
            return redirect('home')
@admin_required
def update_user(request,user_id):
    try:
        user=Myuser.objects.get(id=user_id)
    except:
        return render(request,'something_went_wrong.html')
    if request.method=='GET':
        update_form=UpdateUserForm(instance=user)
        return render(request,'create_user.html',{'form':update_form})
    elif request.method=='POST':
        update_form=UpdateUserForm(request.POST,instance=user)
        if update_form.is_valid():
            try:
                update_form.save()
            except:
                return render(request,'something_went_wrong.html')
            return redirect('home')
@staff_required
def enrollments(request,subject_id):
    try:
        subject=Predmeti.objects.get(id=subject_id)
        student=Role.objects.get(name="Student")
        profesor=Role.objects.get(name="Professor")
        enr=Enrollment.objects.filter(subject=subject).values_list('usr')
    except:
        return render(request,'something_went_wrong.html')
    students=[]
    professors=[]
    for i in enr:
        try:
            tmp=Myuser.objects.get(id=i[0])
        except:
            return render(request,'something_went_wrong.html')
        if tmp.role==student:
            students.append(tmp)
        elif(tmp.role==profesor):
            professors.append(tmp)
    return render(request,'enrollments.html',{"students":students,"professors":professors})
@staff_required
def enroll_list(request,student_id):
    try:
        current_user=Myuser.objects.get(id=student_id)
        subjects=Predmeti.objects.all().order_by('sem_red')
    except:
            return render(request,'something_went_wrong.html')
    
    all_enroll={}
    print(subjects[0])
    try:
        for subject1 in subjects:
            try:
                status=Enrollment.objects.get(subject=subject1,usr=current_user).status.name
            except Enrollment.DoesNotExist:
                status="Nije upisan"
            #print(subject1)
            #print('bla')
            all_enroll[subject1.name]={"semestar":str(subject1.sem_red),"status":status}
    except:
        return render(request,'something_went_wrong.html')
    return render(request,'sub_list.html',{"subjects":all_enroll,"student_id":student_id})
@admin_required
def enroll(request,student_id):
    try:
        enr=Enrollment.objects.filter(usr=student_id).values_list('subject')
        all=Predmeti.objects.all()
    except:
        return render(request,'something_went_wrong.html')
    res_list = [x[0] for x in enr]
    enr_sub=[]
    for subject in all:
        if subject.id not in res_list:
            enr_sub.append(subject.id)
    try:
        enr=Predmeti.objects.filter(pk__in=enr_sub)
    except:
        return render(request,'something_went_wrong.html')
    if request.method=='GET':
        #sub_form=SubjectForm(professors,request.POST or None)
        enr_form=EnrollForm(enr,request.POST or None)
        return render(request,'enroll.html',{"form":enr_form})
    elif request.method=="POST":
        #sub_form=SubjectForm(professors,request.POST)
        enr_form=EnrollForm(enr,request.POST or None)
        if enr_form.is_valid():
            try:
                usr=Myuser.objects.get(id=student_id)
                enr=Enrollment(usr=usr,subject=enr_form.cleaned_data['subject'],status=enr_form.cleaned_data['status'])
                enr.save()
            except:
                return render(request,'something_went_wrong.html')
            return redirect('http://localhost:8000/enrollments/'+str(student_id))




