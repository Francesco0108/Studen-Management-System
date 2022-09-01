from django.shortcuts import render
from django.contrib.auth.hashers import make_password

from .models import *
'''
def init(request):
    r1=Role.objects.get(name='Profesor')
    s1=Status.objects.get(name='Redovni')
    usr1=Myuser(email='nmaroevic@oss.unist.hr',username='nmaroevic',password=make_password('nada'),role=r1,status=s1,first_name='Nada',last_name='Maroevic Roguljic')
    usr2=Myuser(email='sknezevic@oss.unist.hr',username='skenezic',password=make_password('stjepan'),role=r1,status=s1,first_name='Stjepan',last_name='Knezevic')
    usr3=Myuser(email='szorica@oss.unist.hr',username='szorica',password=make_password('sinisa'),role=r1,status=s1,first_name='Sinisa',last_name='Zorica')
    usr4=Myuser(email='ikedzo@oss.unist.hr',username='ikedzo',password=make_password('ivan'),role=r1,status=s1,first_name='Ivan',last_name='Kedzo')
    usr5=Myuser(email='icizmic@oss.unist.hr',username='icizmic',password=make_password('ivana'),role=r1,status=s1,first_name='Ivana',last_name='Cizmic')
    usr6=Myuser(email='amisura@oss.unist.hr',username='amisura',password=make_password('arijana'),role=r1,status=s1,first_name='Arijana',last_name='Misura')
    usr7=Myuser(email='troncevic@oss.unist.hr',username='troncevic',password=make_password('toma'),role=r1,status=s1,first_name='Toma',last_name='Roncevic')
    usr8=Myuser(email='ibaras@oss.unist.hr',username='ibaras',password=make_password('ivo'),role=r1,status=s1,first_name='Ivo',last_name='Baras')
    usr9=Myuser(email='ldespalatovic@oss.unist.hr',username='ldespalatovic',password=make_password('ljiljana'),role=r1,status=s1,first_name='Ljiljana',last_name='Despalatovic')
    usr10=Myuser(email='iruzic@oss.unist.hr',username='iruzic',password=make_password('ivica'),role=r1,status=s1,first_name='Ivica',last_name='Ruzic')
    usr11=Myuser(email='kklarin@oss.unist.hr',username='kklarin',password=make_password('karmen'),role=r1,status=s1,first_name='Karmen',last_name='Klarin')
    usr12=Myuser(email='hbozikovic@oss.unist.hr',username='hbozikovic',password=make_password('haidi'),role=r1,status=s1,first_name='Haidi',last_name='Bozikovic')
    usr13=Myuser(email='ngrgic@oss.unist.hr',username='ngrgic',password=make_password('nikola'),role=r1,status=s1,first_name='Nikola',last_name='Grgic')
    usr14=Myuser(email='tlistes@oss.unist.hr',username='tlistes',password=make_password('tatjana'),role=r1,status=s1,first_name='Tatjana',last_name='Listes')
    usr15=Myuser(email='akrolo@oss.unist.hr',username='akrolo',password=make_password('anita'),role=r1,status=s1,first_name='Anita',last_name='Krolo')
    usr16=Myuser(email='vkozica@oss.unist.hr',username='vkozica',password=make_password('valentini'),role=r1,status=s1,first_name='Valentini',last_name='Kozica')
    usr17=Myuser(email='lreic@oss.unist.hr',username='lreic',password=make_password('lada'),role=r1,status=s1,first_name='Lada',last_name='Reic')
    usr18=Myuser(email='jvrlic@oss.unist.hr',username='jvrlic',password=make_password('josip'),role=r1,status=s1,first_name='Josip',last_name='Vrlic')
    usr19=Myuser(email='mrodic@oss.unist.hr',username='mrodic',password=make_password('marina'),role=r1,status=s1,first_name='Marina',last_name='Rodic')
    usr1.is_staff=True
    usr2.is_staff=True
    usr3.is_staff=True
    usr4.is_staff=True
    usr5.is_staff=True
    usr6.is_staff=True
    usr7.is_staff=True
    usr8.is_staff=True
    usr9.is_staff=True
    usr10.is_staff=True
    usr11.is_staff=True
    usr12.is_staff=True
    usr13.is_staff=True
    usr14.is_staff=True
    usr14.is_staff=True
    usr16.is_staff=True
    usr17.is_staff=True
    usr18.is_staff=True
    usr19.is_staff=True
    usr1.save()
    usr2.save()
    usr3.save()
    usr4.save()
    usr5.save()
    usr6.save()
    usr7.save()
    usr8.save()
    usr9.save()
    usr10.save()
    usr11.save()
    usr12.save()
    usr13.save()
    usr14.save()
    usr15.save()
    usr16.save()
    usr17.save()
    usr18.save()
    usr19.save()

def home(request):
    return render(request,'home.html')
'''

