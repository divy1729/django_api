from django.contrib import admin
from django.urls import include, path
from api.views import StudentviewSet
from rest_framework import routers
router= routers.DefaultRouter()
router.register(r'student',StudentviewSet)
urlpatterns = [
    path('',include(router.urls))
]