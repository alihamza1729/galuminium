from django.conf.urls import url

from .views import (
   CustomerApiView,
   CustomerDetailAPIView,
   CustomerCreateApi,
   CustomerDeleteAPIView,
   CustomerUpdateAPIView,
)

urlpatterns = [
   url(r'^$', CustomerApiView.as_view(), name='list '),
   url(r'^(?P<pk>[0-9]+)/$', CustomerDetailAPIView.as_view(), name='detail'),
   url(r'^(?P<pk>[0-9]+)/edit/$', CustomerUpdateAPIView.as_view(), name='update'),
   url(r'^(?P<pk>[0-9]+)/delete/$', CustomerDeleteAPIView.as_view(), name='delete'),
   url(r'^create/$', CustomerCreateApi.as_view(), name='create'),
]