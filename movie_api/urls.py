from django.urls import path, include
from rest_framework import routers

from cinema.views import MovieView

router = routers.DefaultRouter()
router.register("movie", MovieView)

urlpatterns = [
    path("api/", include(router.urls)),
]
