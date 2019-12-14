from rest_framework import status
from rest_framework.generics import (ListAPIView,
                                     CreateAPIView,
                                     RetrieveAPIView,
                                     DestroyAPIView,
                                     UpdateAPIView)
from rest_framework.response import Response

from ..models import Section
from .serializers import SectionSerializers



class SectionApiView(ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializers


class SectionCreateApi(CreateAPIView):
      queryset = Section.objects.all()
      serializer_class = SectionSerializers

      def post(self, request):
          print(request.data)
          serializer = SectionSerializers(data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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