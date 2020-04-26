from .models import SubPerson

from rest_framework import serializers


class SerializerSubPerson(serializers.ModelSerializer):

    class Meta:
        model = SubPerson
        fields = "__all__"
