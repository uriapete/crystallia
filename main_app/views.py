from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView,RedirectView
from main_app.models import CrystalType,Crystal,Collection

# Create your views here.

class Home(RedirectView):
    query_string=True
    pattern_name="crystal_type_list"


class CrystalTypeListView(ListView):
    model = CrystalType
    template_name = "crystal_type/crystal_type_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["crystaltypes"] = CrystalType.objects.all()
        return context
    
class CrystalTypeCreateView(CreateView):
    model = CrystalType
    fields=['name','mohs_hardness','usual_color','img','bio']
    template_name = "crystal_type/crystal_type_create.html"
    
    
class CrystalTypeDetailView(DetailView):
    model = CrystalType
    template_name = "crystal_type/crystal_type_detail.html"
    
    
class CrystalTypeUpdateView(UpdateView):
    model = CrystalType
    fields=['name','mohs_hardness','usual_color','img','bio']
    template_name = "crystal_type/crystal_type_update.html"
    
    
class CrystalTypeDeleteView(DeleteView):
    model = CrystalType
    template_name = "crystal_type/crystal_type_delete.html"
    success_url="/crystal_types"
    
    
class CrystalListView(ListView):
    model = Crystal
    template_name = "crystal/crystal_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["crystals"] = Crystal.objects.all()
        return context
    
class CrystalCreateView(CreateView):
    model = Crystal
    fields=['type','mohs_hardness','color','img','summary','found_on']
    template_name = "crystal/crystal_create.html"
    
    
class CrystalDetailView(DetailView):
    model = Crystal
    template_name = "crystal/crystal_detail.html"
    
    
class CrystalUpdateView(UpdateView):
    model = Crystal
    fields=['type','mohs_hardness','color','img','summary','found_on']
    template_name = "crystal/crystal_update.html"
    
    
class CrystalDeleteView(DeleteView):
    model = Crystal
    template_name = "crystal/crystal_delete.html"
    success_url="/crystals"
    
    
class CollectionListView(ListView):
    model = Collection
    template_name = "collection/collection_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["collections"] = Collection.objects.all()
        return context
    
class CollectionCreateView(CreateView):
    model = Collection
    fields=['title','crystals','bio',]
    template_name = "collection/collection_create.html"
    
    
class CollectionDetailView(DetailView):
    model = Collection
    template_name = "collection/collection_detail.html"
    
    
class CollectionUpdateView(UpdateView):
    model = Collection
    fields=['title','crystals','bio',]
    template_name = "collection/collection_update.html"
    
    
class CollectionDeleteView(DeleteView):
    model = Collection
    template_name = "collection/collection_delete.html"
    success_url="/collections"


