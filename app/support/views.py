import json
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.core.serializers import serialize
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.views.generic.edit import UpdateView
from .models import FAQModel, AssistanceModel, FeedbackModel
from .forms import AssistanceForm, FeedbackForm


class FAQView(TemplateView):
    "Template: Preguntas Frecuentes"

    template_name="support/faq.html"

class FAQListView(ListView):
    "Petición ajax: Preguntas Frecuentes"

    model=FAQModel
    queryset=model.objects.all()

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            data=serialize("json", self.queryset)
            return HttpResponse(data, "application/json")
        
        else:    
            return redirect("support:faq")


class AssistanceView(TemplateView):
    "Asesoría personalizada "
    
    template_name="support/assistance/assistance.html"


class AssistanceListView(ListView):
    "Lista de asesoría solicitada"
    model=AssistanceModel
    template_name="support/assistance/list.html"
    context_object_name="assistance"

class AssistanceCreateView(CreateView):
    "Crear Asesoría personalizada"

    model=AssistanceModel
    form_class=AssistanceForm
    template_name="support/assistance/create.html"
    context_object_name="form"
    success_url=reverse_lazy("support:assistance")

class AssistanceUpdateView(UpdateView):
    "Actualizar asesoría"

    model=AssistanceModel
    form_class=AssistanceForm
    template_name="support/assistance/update.html"
    context_object_name="form"
    success_url=reverse_lazy("support:assistance_list")

class FeedbackView(CreateView):
    "Creación de comentarios a través de AJAX"
    
    model=FeedbackModel
    form_class=FeedbackForm
    template_name="support/feedback/index.html"
    context_object_name="form"
    
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form=self.form_class(data=request.POST)
            if form.is_valid():
                feedback=FeedbackModel(
                        issue=form.cleaned_data.get("issue"),
                        description=form.cleaned_data.get("description"),
                        user=request.user
                )
                feedback.save()
                
                "Variables AJAX"
                message="se registro correctamente "
                #message=f'{self.model.__name__} registrado correctamente'
                error="No hay error"
                response=JsonResponse({'mensaje':message, "error":error})
                response.status_code=201
                return response
            else:
                message="no se registro correctamente"
                error=form.errors
                response=JsonResponse({'mensaje':message, "error":error})
                response.status_code=400
                return response
        else:
            return redirect("support:feedback")
    
    
    

