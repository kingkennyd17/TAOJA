from django.urls import path
from . import views

urlpatterns = [
    path("phone/", views.PhoneListCreate.as_view(), name="home"),
    path("phone/<int:pk>/", views.PhoneRetrieveUpdateDestroy.as_view(), name="update")
]