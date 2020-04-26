from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ViewTheClassFull,  ViewTheClass, ViewMembership, ViewImage, ViewVideo, ViewOpinion

router = DefaultRouter()


router.register("the-class-full", ViewTheClassFull)

# base
router.register("the-class", ViewTheClass)
router.register("membership", ViewMembership)
router.register("image", ViewImage)
router.register("video", ViewVideo)
router.register("opinions", ViewOpinion)


urlpatterns = [


]
urlpatterns += router.urls
