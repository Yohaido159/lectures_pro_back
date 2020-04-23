from django.contrib import admin

from .models import TheClass, Membership, Image, Video, Opinions

MyModels = [TheClass, Membership, Image, Video, Opinions]

admin.site.register(MyModels)
