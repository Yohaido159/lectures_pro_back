from rest_framework import serializers

from .models import User
from classes.serializers import SerializerClass, SerializerClassId


class SerializerUser(serializers.ModelSerializer):
    the_classes = SerializerClassId(many=True, read_only=True)

    class Meta:
        model = User
        fields = ("id", "email", "name", "phone", "the_classes")
