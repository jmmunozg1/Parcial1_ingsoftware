from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.core.exceptions import ValidationError
from .models import Flight

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'vuelos/home.html'

class FlightPageView(TemplateView): 
    template_name = 'vuelos/index.html' 
     
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context.update({ 
            "title": "About us - Online Store", 
            "subtitle": "About us", 
            "description": "This is an about page ...", 
            "author": "Developed by: Juan Miguel", 
        }) 
 
        return context

class FlightForm(forms.ModelForm): 
    
    class Meta:
        model = Flight
        fields = ['name','type','price']

    def clean_price(self): #clean_<fieldname>
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError('The price must be greater than zero.')
        return price

class FlightCreateView(View): 
    template_name = 'vuelos/create.html' 
 
    def get(self, request): 
        form = FlightForm() 
        viewData = {} 
        viewData["title"] = "Register flight" 
        viewData["form"] = form 
        return render(request, self.template_name, viewData) 
 
    def post(self, request): 
        form = FlightForm(request.POST) 
        if form.is_valid(): 
            form.save()
            return redirect('home')  
        else: 
            viewData = {} 
            viewData["title"] = "Register fight" 
            viewData["form"] = form 
            return render(request, self.template_name, viewData)
        
class FlightListView(ListView):
    model = Flight
    template_name = 'vuelos/list.html'
    context_object_name = 'flights' #Permite recorrer 'productos' en el template. Se usa en el html.
    ordering = ['price']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']  = 'Products - Online Store'
        context['subtitle'] = 'List of flights'

        return context