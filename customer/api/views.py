from rest_framework import status
from rest_framework.generics import (ListAPIView,
                                     CreateAPIView,
                                     RetrieveAPIView,
                                     DestroyAPIView,
                                     UpdateAPIView)
from rest_framework.response import Response
from ..models import Customer

from .serializers import CustomerSerializers


class CustomerApiView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers


def get(request):
    print(request.data)
    serializer = CustomerSerializers(data=request.data)
    return Response(serializer.data)


class CustomerCreateApi(CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers

    def post(self, request):
        print(request.data)
        serializer = CustomerSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CustomerDetailAPIView(RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers


class CustomerUpdateAPIView(UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers


class CustomerDeleteAPIView(DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers
