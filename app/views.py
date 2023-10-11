from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import *
from django import forms


class CarsView(ListView):
    model = Car
    template_name = 'home.html'
    context_object_name = 'cars'
    paginate_by = 4

class AboutCar(DetailView):
    model = Car
    template_name = 'about.html'
    context_object_name = 'car'

class CreateCar(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'create.html'
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        data = CarForm(request.POST)
        x = int(request.POST['year'])
        if x > 2023:
            message = "Модель должна быть не позднее 2023 года"
            raise forms.ValidationError(message)
        else:
            data.save()
        return redirect('home')

"""def insert(request):
    if request.method == 'POST':

        one = request.POST
        print(one)
        add_f1teams = Formula1Teams.objects.create(name=one['name'], country=one['country'], driver1=one['driver1'], driver2=one['driver2'], car=one['car'])
        x = Formula1Teams(name=one['name'], country=one['country'], driver1=one['driver1'], driver2=one['driver2'], car=one['car'])
        if x.year > 2023:
            raise forms.ValidationError(msg)
        else
        add_f1teams.save()
        return redirect('home')
    else:
        return render(request, 'insert.html')"""

class DeletePicture(DeleteView):    
    model = Car
    template_name = 'delete.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('home')