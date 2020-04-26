from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ViewUser

router = DefaultRouter()
router.register("user", ViewUser)
urlpatterns = [

]

urlpatterns += router.urls
