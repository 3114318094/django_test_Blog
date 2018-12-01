from django.conf.urls import url

from Blog import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.blog_title, name='blog_title'),
    url('(?P<post_id>\d)',views.blog_detail,name='blog_detail'),
]
