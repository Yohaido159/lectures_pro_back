from django.shortcuts import render

from rest_framework import viewsets

from .serializers import SerializerTheClassFull, SerializerClass, SerializerMembership, SerializerImage, SerializerVideo, SerializerOpinion
from .models import TheClass, Membership, Image, Video, Opinion

from users.models import User
from users.serializers import SerializerUser
# BASE


class ViewTheClass(viewsets.ModelViewSet):
    queryset = TheClass.objects.all()
    serializer_class = SerializerClass


class ViewMembership(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = SerializerMembership


class ViewImage(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = SerializerImage


class ViewVideo(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = SerializerVideo


class ViewOpinion(viewsets.ModelViewSet):
    queryset = Opinion.objects.all()
    serializer_class = SerializerOpinion


# FULL
class ViewTheClassFull(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SerializerTheClassFull
