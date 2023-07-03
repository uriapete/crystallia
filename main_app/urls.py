from django.urls import path
from . import views

urlpatterns = [
    path("crystal_types/",view=views.CrystalTypeListView.as_view(),name="crystal_type_list"),
    path("crystal_types/add/",view=views.CrystalTypeCreateView.as_view(),name="crystal_type_create"),
    path("crystal_types/<int:pk>/",view=views.CrystalTypeDetailView.as_view(),name="crystal_type_detail"),
    path("crystal_types/<int:pk>/update",view=views.CrystalTypeUpdateView.as_view(),name="crystal_type_update"),
    path("crystal_types/<int:pk>/delete",view=views.CrystalTypeDeleteView.as_view(),name="crystal_type_delete"),
]
