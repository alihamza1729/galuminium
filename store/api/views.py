from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView)

from ..models import Store

from .serializers import StoreSerializers


class StoreApiView(ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializers


class StoreCreateApi(CreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializers


class StoreDetailAPIView(RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializers


class StoreUpdateAPIView(UpdateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializers


class StoreDeleteAPIView(DestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializers
