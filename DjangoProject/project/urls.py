from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_project, name="all_project"),
    path("<int:chai_id>", views.chai_details, name="chai_details"),
]
