from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from main_app.models import Crystal

# Create your views here.
class CrystalListView(ListView):
    model = Crystal
    template_name = "crystal/crystal_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["crystals"] = Crystal.objects.all()
        return context
    
    
class CrystalCreateView(CreateView):
    model = Crystal
    fields=['name','mohs_hardness','usual_color','img','bio']
    template_name = "crystal/crystal_create.html"
    
    
class CrystalDetailView(DetailView):
    model = Crystal
    template_name = "crystal/crystal_detail.html"
    
    
class CrystalUpdateView(UpdateView):
    model = Crystal
    fields=['name','mohs_hardness','usual_color','img','bio']
    template_name = "crystal/crystal_update.html"
    
    
class CrystalDeleteView(DeleteView):
    model = Crystal
    template_name = "crystal/crystal_delete.html"
    success_url="/crystals"


