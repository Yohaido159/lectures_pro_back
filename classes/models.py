from django.db import models

from users.models import User
from sub_persones.models import SubPerson


def get_image_fk(instance, filename):
    main_person = instance.belongs_to.main_person.name
    the_class = instance.belongs_to.class_name
    return f"{main_person}/{the_class}/images/{filename}"


def get_video_fk(instance, filename):
    main_person = instance.belongs_to.main_person.name
    the_class = instance.belongs_to.class_name
    return f"{main_person}/{the_class}/video/{filename}"


class TheClass(models.Model):
    class_name = models.CharField(max_length=120, blank=True, null=True)
    main_person = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="the_classes")
    sub_persones = models.ManyToManyField(SubPerson, through="Membership", through_fields=("the_class", "the_sub_person"),  related_name="A", blank=True)
    start_at = models.DateTimeField(blank=True, null=True)
    available = models.CharField(max_length=50, blank=True, null=True)
    is_done = models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def check_if_done(self):
        pass
        # TODO

    def __str__(self):
        return self.class_name


class Membership(models.Model):
    class Meta:
        db_table = "classes_A_the_sub_person"

    the_class = models.ForeignKey(TheClass, on_delete=models.CASCADE, blank=True, null=True, related_name="members")
    the_sub_person = models.ForeignKey(SubPerson, on_delete=models.CASCADE, blank=True, null=True, related_name="member")
    join_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.the_class.class_name


class Image(models.Model):
    image_file = models.ImageField(upload_to=get_image_fk, blank=True, null=True)
    belongs_to = models.ForeignKey(TheClass, on_delete=models.CASCADE, related_name="images")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.image_file.name


class Video(models.Model):
    video_file = models.FileField(upload_to=get_video_fk, blank=True, null=True)
    belongs_to = models.ForeignKey(TheClass, on_delete=models.CASCADE, related_name="videos")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.video_file.name


class Opinion(models.Model):
    sub_person = models.ForeignKey(SubPerson, on_delete=models.CASCADE)
    the_class = models.ForeignKey(TheClass, on_delete=models.CASCADE, related_name="opinions")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sub_person.name}: {self.content[:50]}"
