from rest_framework.generics import (ListAPIView,
                                     CreateAPIView,
                                     RetrieveAPIView,
                                     DestroyAPIView,
                                     UpdateAPIView)

from ..models import Section
from .serializers import SectionSerializers



class SectionApiView(ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializers


class SectionCreateApi(CreateAPIView):
      queryset = Section.objects.all()
      serializer_class = SectionSerializers





class SectionDetailAPIView(RetrieveAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializers


class SectionUpdateAPIView(UpdateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializers


class SectionDeleteAPIView(DestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializers


# if Section.objects.filter(section_name="D29", section_thickness="0.9", section_color="dull"):
#     qs = Section.objects.values(section_rate = "section_rate")
#     print(qs)