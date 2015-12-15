# coding=utf-8
from django.conf.urls import include, url, patterns

urlpatterns = patterns(
    '',
    url(r'^v1/', include('bosque.v1.urls', namespace='v1')),
)
