from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView,RedirectView
from main_app.models import CrystalType

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


