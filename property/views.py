from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView , CreateView
from .models import Property
from django.views.generic.edit import FormMixin
from .forms import PropertyBookForm
from .filter import PropertyFilter
from django_filters.views import FilterView

# Create your views here.

class PropertyList(FilterView):
    model = Property
    paginate_by = 3
    filterset_class = PropertyFilter
    template_name = 'property/property_list.html'

    # template_name = 'property/property_list.html'
    # context_object_name = 'properties'

class PropertyDetail(FormMixin,DetailView):
    model = Property
    form_class = PropertyBookForm
    # template_name = 'property/property_detail.html'
    # context_object_name = 'property'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related'] = Property.objects.filter(category=self.get_object().category)[:2]
        return context
    
    def post(self,request,*args,**kwargs):
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=False)
            myform.property = self.get_object()
            myform.user = request.user
            myform.save()    
            return redirect('/')
        
        else:
            print('not valid')
            
            
# class AddListing(CreateView):
#     model = Property
#     # template_name = 'property/add_listing.html'
#     # fields = ['title','description','price','location','category','image']
#     # success_url = '/property/listing'
#     # def form_valid(self,form):
#     #     form.instance.user = self.request.user
#     #     return super().form_valid(form)
#     # def form_invalid(self,form):
        
               
            
            
            
            
            
            