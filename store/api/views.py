from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView)

from rest_framework.response import Response
from ..models import Store

from .serializers import StoreSerializers


class StoreApiView(ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializers


class StoreCreateApi(CreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializers

    def post(self, request):
        print(request.data)
        serializer = StoreSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StoreDetailAPIView(RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializers


class StoreUpdateAPIView(UpdateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializers


class StoreDeleteAPIView(DestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializers
