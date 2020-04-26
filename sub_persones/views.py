
from rest_framework import viewsets
from .serializers import SerializerSubPerson
from .models import SubPerson


class ViewSubPerson(viewsets.ModelViewSet):
    queryset = SubPerson.objects.all()
    serializer_class = SerializerSubPerson
