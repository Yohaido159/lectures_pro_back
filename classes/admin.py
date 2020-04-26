from django.contrib import admin

from .models import TheClass, Membership, Image, Video, Opinion

from sub_persones.models import SubPerson


class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 0


class AdminTheClass(admin.ModelAdmin):
    inlines = (MembershipInline,)


class AdminSubPerson(admin.ModelAdmin):
    inlines = (MembershipInline,)


admin.site.register(TheClass, AdminTheClass)
admin.site.register(SubPerson, AdminSubPerson)
admin.site.register(Membership)
admin.site.register(Image)
admin.site.register(Video)
admin.site.register(Opinion)
