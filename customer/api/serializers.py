from rest_framework.serializers import ModelSerializer

from ..models import Customer


class CustomerSerializers(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'