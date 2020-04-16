from django.conf.urls import url
from lists import views
from django.urls import path, include
from django.contrib import admin


#from superlists

urlpatterns = [
    path('', views.user_count, name='userCount'),
    path('calGrade', views.cal_grade,name='calGrade'),
    path('admin/', admin.site.urls),
    path('signup', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'home', views.home_page, name='home'),
    url(r'flow', views.flow, name='flow'),
    url(r'help', views.help, name='help'),
    url(r'subject', views.list_of_subject, name='listOfSubjects'),
    url(r'graph', views.graph, name='Graph'),
    url(r'picFlow', views.pic_flow, name='picFlow'),
    url(r'firstTerm', views.first_term_result, name='firstTerm'),
    url(r'secondTerm', views.second_term_result, name='secondTerm'),
    url(r'thirdTerm', views.third_term_result, name='thirdTerm'),
    url(r'fourthTerm', views.fourth_term_result, name='fourthTerm'),
    url(r'fifthTerm', views.fifth_term_result, name='fifthTerm'),
    url(r'sixthTerm', views.sixth_term_result, name='sixthTerm'),
    url(r'seventhTerm', views.seventh_term_result, name='seventhTerm'),
    url(r'eightTerm', views.eight_term_result, name='eightTerm'),
    url(r'about', views.about, name='about'),


]
