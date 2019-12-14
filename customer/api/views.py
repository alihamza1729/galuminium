from rest_framework.generics import (ListAPIView,
                                     CreateAPIView,
                                     RetrieveAPIView,
                                     DestroyAPIView,
                                     UpdateAPIView)
from ..models import Customer

from .serializers import CustomerSerializers


class CustomerApiView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers


class CustomerCreateApi(CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers


class CustomerDetailAPIView(RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers


class CustomerUpdateAPIView(UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers


class CustomerDeleteAPIView(DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers
