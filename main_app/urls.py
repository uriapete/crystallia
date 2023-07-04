from django.urls import path
from . import views

urlpatterns = [
    path("",view=views.Home.as_view(),name='home'),
    path("crystal_types/",view=views.CrystalTypeListView.as_view(),name="crystal_type_list"),
    path("crystal_types/add/",view=views.CrystalTypeCreateView.as_view(),name="crystal_type_create"),
    path("crystal_types/<int:pk>/",view=views.CrystalTypeDetailView.as_view(),name="crystal_type_detail"),
    path("crystal_types/<int:pk>/update",view=views.CrystalTypeUpdateView.as_view(),name="crystal_type_update"),
    path("crystal_types/<int:pk>/delete",view=views.CrystalTypeDeleteView.as_view(),name="crystal_type_delete"),
    path("crystals/",view=views.CrystalListView.as_view(),name="crystal_list"),
    path("crystals/add/",view=views.CrystalCreateView.as_view(),name="crystal_create"),
    path("crystals/<int:pk>/",view=views.CrystalDetailView.as_view(),name="crystal_detail"),
    path("crystals/<int:pk>/update",view=views.CrystalUpdateView.as_view(),name="crystal_update"),
    path("crystals/<int:pk>/delete",view=views.CrystalDeleteView.as_view(),name="crystal_delete"),
    path("collections/",view=views.CollectionListView.as_view(),name="collection_list"),
    path("collections/add/",view=views.CollectionCreateView.as_view(),name="collection_create"),
    path("collections/<int:pk>/",view=views.CollectionDetailView.as_view(),name="collection_detail"),
    path("collections/<int:pk>/update",view=views.CollectionUpdateView.as_view(),name="collection_update"),
    path("collections/<int:pk>/delete",view=views.CollectionDeleteView.as_view(),name="collection_delete"),
]
