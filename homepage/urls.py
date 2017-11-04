from django.conf.urls import url

from . import views

app_name = 'home'

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'testing/', views.testing_space, name='testing_space'),
        url(r'about/', views.about, name='about'),
        ]
