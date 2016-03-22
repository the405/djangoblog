from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.index, name='index'),
    url(r'^portfolio/', views.portfolio, name='portfolio'),
    url(r'^blog/', views.blog, name='blog'),
    url(r'^about/', views.about, name='about'),
]
