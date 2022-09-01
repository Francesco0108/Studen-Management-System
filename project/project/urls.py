"""
project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from elearning import views
from elearning import views
from elearning import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.root),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('home/',views.home,name='home'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('subject/<int:subject_id>',views.subject_details,name='subject_details'),
    path('changesubjectstatus/<int:subject_id>/<int:student_id>/<int:status_id>/',views.change_subject_status),
    path('createsubject/',views.create_subject),
    path('updatesubject/<int:subject_id>',views.update_subject),
    path('createuser/',views.create_user),
    path('updateuser/<int:user_id>/',views.update_user),
    path('users/<int:subject_id>/',views.subject_users),
    path('enrollments/<int:student_id>/',views.enroll_list),
    path('enroll/<int:student_id>/',views.enroll),
    path('unenroll/<int:subject_id>/',views.unenroll),
    path('staffunenroll/<int:subject_id>/<int:user_id>/',views.staff_unenroll),
    path('deletesubject/<int:subject_id>/',views.delete_subject)
]
