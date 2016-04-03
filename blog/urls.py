from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^portfolio/', views.portfolio, name='portfolio'),
    url(r'^blog/', views.blog, name='blog'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^about/', views.about, name='about'),
    url(r'^', views.index, name='index'),
]
