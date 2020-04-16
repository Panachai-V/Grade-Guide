from django.conf.urls import url
from lists import views
from django.urls import path, include
from django.contrib import admin


#from superlists

urlpatterns = [
    path('', views.userCount, name='userCount'),
    path('calGrade', views.calGrade,name='calGrade'),
    path('termselect', views.termselect,name='termselect'),
    path('admin/', admin.site.urls),
    path('signup', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'home', views.home_page, name='home'),
    url(r'flow', views.flow, name='flow'),
    url(r'help', views.help, name='help'),
    url(r'subject', views.listOfSubject, name='listOfSubjects'),
    url(r'graph', views.Graph, name='Graph'),
    url(r'picFlow', views.picFlow, name='picFlow'),
    url(r'firstTerm', views.firstTermResult, name='firstTerm'),
    url(r'secondTerm', views.secondTermResult, name='secondTerm'),
    url(r'thirdTerm', views.thirdTermResult, name='thirdTerm'),
    url(r'fourthTerm', views.fourthTermResult, name='fourthTerm'),
    url(r'fifthTerm', views.fifthTermResult, name='fifthTerm'),
    url(r'sixthTerm', views.sixthTermResult, name='sixthTerm'),
    url(r'seventhTerm', views.seventhTermResult, name='seventhTerm'),
    url(r'eightTerm', views.eightTermResult, name='eightTerm'),
    url(r'about', views.about, name='about'),
    #url(r'home', views.home_page, name='calGrade'),
    #admin page
    #path('admin/', admin.site.urls),
    #url(r'^admin/', admin.site.urls),
    #register path
    #path("register/", v.register, name="register"),


]
