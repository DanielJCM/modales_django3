# -*- coding: utf-8 -*-
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from app.models import Person
from app.forms import PersonForm
from django.shortcuts import render


class Index(TemplateView):
    """
    Class that shows the start template.
    """
    template_name = "app/index.html"


class List(ListView):
    """
    Class that lists the Person objects.
    """
    model = Person


class Create(CreateView):
    """
    Class that allows you to create and save a Person object.
    """
    model = Person
    form_class = PersonForm
    #fields = ['first_name', 'last_name']
    success_url = reverse_lazy('list')


class Update(UpdateView):
    """
    Class that allows you to update the data of a Person object.
    """
    model = Person
    form_class = PersonForm
    template_name = "app/person_update.html"
    #fields = ['first_name', 'last_name']
    success_url = reverse_lazy('list')


class Delete(DeleteView):
    """
    Class that allows you to delete a Person object.
    """
    model = Person
    success_url = reverse_lazy('list')

class Detail(DetailView):
    """
    Class that allows you to see the details of a Person object
    """
    model = Person
    template_name = 'app/person_detail.html'

# Create your views here.
