from django.conf.urls import url

from .views import (SectionApiView,
                    SectionDetailAPIView,
                    SectionCreateApi,
                    SectionDeleteAPIView,
                    SectionUpdateAPIView)

urlpatterns = [
    url(r'^$', SectionApiView.as_view(), name='list '),
    url(r'^(?P<pk>[0-9]+)/$', SectionDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/edit/$', SectionUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', SectionDeleteAPIView.as_view(), name='delete'),
    url(r'^create/$', SectionCreateApi.as_view(), name='create'),
]
