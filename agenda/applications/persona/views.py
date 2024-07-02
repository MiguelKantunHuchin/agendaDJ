from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import Person, Reunion

# * las importaciones y formas de trabajar son similares con rest_framework
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)
from .serializer import (
    PersonSerializer,
    PersonaSerializer,
    ReunionSerializer,
    PersonSerializer2,
    ReunionSerializer2,
    CountReunionSerializer,
)


# * Esto es como normalmente se trabajaba con django normalito
class ListaPersonasView(ListView):
    context_object_name = "personas"
    template_name = "persona/personas.html"

    def get_queryset(self):
        return Person.objects.all()


# * Esta es la forma de trabajar con rest_framework
class PersonListApiView(ListAPIView):

    serializer_class = PersonSerializer2

    def get_queryset(self):
        return Person.objects.all()


#! Esto solo es una demostración con Vue.js
class PersonView(TemplateView):
    template_name = "persona/lista.html"


# * Clase para buscar
class PersonSearchApiView(ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        kword = self.kwargs["kword"]
        return Person.objects.filter(full_name__icontains=kword)


class PersonCreateView(CreateAPIView):
    serializer_class = PersonSerializer


# * El retrive es el equivalente al detailview
class PersonDetailView(RetrieveAPIView):
    # * Síemrpe necestia 2 parámetros
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


# * El destroy es el equivalente al deleteview
class PersonDeleteView(DestroyAPIView):
    serializer_class = PersonSerializer
    # * Con el queryset es el equivalente a model del delete / detail
    queryset = Person.objects.all()


# * Este Update solo muestra un formulario con los campos pero están vacíos :( :D:
class PersonUpdateView(UpdateAPIView):
    serializer_class = PersonSerializer
    # * Con el queryset es el equivalente a model del delete / detail / update
    queryset = Person.objects.all()


# * Este muestra el formulario pero con los datos ya llenos
class PersonRetriveUpdateView(RetrieveUpdateAPIView):
    serializer_class = PersonSerializer
    # * Con el queryset es el equivalente a model del delete / detail / update
    queryset = Person.objects.all()


class PersonApiLista(ListAPIView):
    serializer_class = PersonaSerializer

    def get_queryset(self):
        return Person.objects.all()


class ReunionApiLista(ListAPIView):
    serializer_class = ReunionSerializer2

    def get_queryset(self):
        return Reunion.objects.all()


class ReunionByJobs(ListAPIView):
    serializer_class = CountReunionSerializer

    def get_queryset(self):
        return Reunion.objects.cantidad_reuniones_job()
