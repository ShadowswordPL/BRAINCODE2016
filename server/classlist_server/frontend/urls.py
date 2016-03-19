from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^student/(?P<student_id>\d+)', views.student, name='student'),
    url(r'^students$', views.students, name='students'),
    url(r'^lesson/(?P<lesson_id>\d+)', views.lesson, name='lesson'),
    url(r'^lessons$', views.lessons, name='lessons'),
    url(r'^how_it_works$', views.how_it_works, name='how_it_works'),
]
