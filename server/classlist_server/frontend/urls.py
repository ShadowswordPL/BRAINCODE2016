from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^students$', views.students, name='students'),
    url(r'^lessons$', views.lessons, name='lessons'),
    url(r'^how_it_works$', views.how_it_works, name='how_it_works'),
]
