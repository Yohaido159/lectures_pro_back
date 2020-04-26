from django.contrib import admin

from .models import TheClass, Membership, Image, Video, Opinion

MyModels = [TheClass, Membership, Image, Video, Opinion]

admin.site.register(MyModels)
