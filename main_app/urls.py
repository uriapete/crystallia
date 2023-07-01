from django.urls import path
from . import views

urlpatterns = [
    path("crystals/",view=views.CrystalListView.as_view(),name="crystal_list"),
    path("crystals/add/",view=views.CrystalCreateView.as_view(),name="crystal_create"),
    path("crystals/<int:pk>/",view=views.CrystalDetailView.as_view(),name="crystal_detail"),
    path("crystals/<int:pk>/update",view=views.CrystalUpdateView.as_view(),name="crystal_update"),
    path("crystals/<int:pk>/delete",view=views.CrystalDeleteView.as_view(),name="crystal_delete"),
]
