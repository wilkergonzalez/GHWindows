from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("author/", views.author),
    path("<int:owner_id>/", views.detail, name="detail"),
    path("owner/<str:owner_name>/", views.name),
    path("details/<int:cat_id>/", views.catsdetail, name="catdetail"),
    path("owners/", views.owners),
    path("owner-name/", views.owner_name)
]

