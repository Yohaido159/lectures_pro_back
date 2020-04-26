from rest_framework import serializers

from .models import TheClass, Membership, Image, Video, Opinion

# from users.serializers import SerializerUser
from users.models import User
from sub_persones.serializers import SerializerSubPerson
from sub_persones.models import SubPerson


# BASE
class SerializerMembership(serializers.ModelSerializer):
    # the_sub_person = serializers.CharField(source="the_sub_person.name")
    the_sub_person = SerializerSubPerson()

    class Meta:
        model = Membership
        # fields = "__all__"
        exclude = ["id"]


class SerializerImage(serializers.ModelSerializer):
    belongs_to = serializers.CharField(source="belongs_to.class_name")

    class Meta:
        model = Image
        fields = "__all__"


class SerializerVideo(serializers.ModelSerializer):
    belongs_to = serializers.CharField(source="belongs_to.class_name")

    class Meta:
        model = Video
        fields = "__all__"


class SerializerOpinion(serializers.ModelSerializer):
    sub_person = serializers.CharField(source="sub_person.name")

    class Meta:
        model = Opinion
        fields = "__all__"


class SerializerClass(serializers.ModelSerializer):

    # sub_persones = SerializerSubPerson(many=True, read_only=True)
    images = SerializerImage(many=True, read_only=True)
    videos = SerializerVideo(many=True, read_only=True)
    opinions = SerializerOpinion(many=True, read_only=True)
    members = SerializerMembership(many=True, read_only=True)

    class Meta:
        model = TheClass
        fields = "__all__"


class SerializerClassId(serializers.ModelSerializer):
    class Meta:
        model = TheClass
        fields = ("id",)


# THE FULL CLASS
class SerializerTheClassFull(serializers.ModelSerializer):
    the_classes = SerializerClass(many=True, read_only=True)

    class Meta:
        model = User
        fields = ("id", "email", "name", "phone", "the_classes")
