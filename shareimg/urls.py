from django.conf.urls import include, url
from shareimg import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'image_share.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.upload, name = "main"),
    url(r'^handl/$', views.hnd_load, name = "handl"),
]
