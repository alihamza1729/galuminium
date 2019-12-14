from rest_framework.serializers import ModelSerializer

from ..models import Section


class SectionSerializers(ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'