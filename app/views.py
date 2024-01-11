from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView,  UpdateView, DetailView, DeleteView
from app.models import Cliente

class ClienteList(ListView):
    model = Cliente
    queryset = Cliente.objects.all()
    
    
class ClienteCreate(CreateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('app:list')
    
class ClienteUpdate(UpdateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('app:list')
    
class ClienteDetail(DetailView):
    model = Cliente
    queryset = Cliente.objects.all()
    
class ClienteDelete(DeleteView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('app:list')
    
    