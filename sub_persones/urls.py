from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import ViewSubPerson

router = DefaultRouter()
router.register("sub-person", ViewSubPerson)
urlpatterns = [

]

urlpatterns += router.urls
