from django.conf.urls import include, url
from shareimg import urls as appurls
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from .settings import MEDIA_URL, MEDIA_ROOT
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'image_share.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(appurls)),
    url(r'^admin/', admin.site.urls),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += patterns('',
#         (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#         'document_root': settings.MEDIA_ROOT}))