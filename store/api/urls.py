from django.conf.urls import url

from .views import (
    StoreApiView,
    StoreDetailAPIView,
    StoreCreateApi,
    StoreDeleteAPIView,
    StoreUpdateAPIView,
)

urlpatterns = [
    url(r'^$', StoreApiView.as_view(), name="list"),
    url(r'^create/$', StoreCreateApi.as_view(), name="create"),
    url(r'^(?P<pk>[0-9]+)/$', StoreDetailAPIView.as_view(), name="detail"),
    url(r'^(?P<pk>[0-9]+)/edit/$', StoreUpdateAPIView.as_view(), name="update"),
    url(r'^(?P<pk>[0-9]+)/delete/$', StoreDeleteAPIView.as_view(), name="delete"),
]
