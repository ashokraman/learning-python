from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /post/
    url(r'^$', views.post_list, name='post_list'),
    # ex: /post/5/
    url(r'^(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]