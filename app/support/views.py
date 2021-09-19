import json
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.core.serializers import serialize
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.views.generic.edit import UpdateView
from app.support.models import FAQModel, AssistanceModel, FeedbackModel
from app.support.forms import AssistanceForm, FeedbackForm


class FAQView(TemplateView):
    """Template:FAQ
        
        
        :TemplateView: django view
    """

    template_name="support/faq.html"

class FAQListView(ListView):
    """FAQ
        Ajax request
        
        :ListView: django view
    """

    model=FAQModel
    queryset=model.objects.all()

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            data=serialize("json", self.queryset)
            return HttpResponse(data, "application/json")
        
        else:    
            return redirect("support:faq")


class AssistanceView(TemplateView):
    "Support template"
    
    template_name="support/assistance/assistance.html"


class AssistanceListView(ListView):
    "Support List"
    
    model=AssistanceModel
    template_name="support/assistance/list.html"
    context_object_name="assistance"

class AssistanceCreateView(CreateView):
    "Create support"

    model=AssistanceModel
    form_class=AssistanceForm
    template_name="support/assistance/create.html"
    context_object_name="form"
    success_url=reverse_lazy("support:assistance")

class AssistanceUpdateView(UpdateView):
    """Update support
    
    
        :UpdateView: django view
    """

    model=AssistanceModel
    form_class=AssistanceForm
    template_name="support/assistance/update.html"
    context_object_name="form"
    success_url=reverse_lazy("support:assistance_list")

class FeedbackView(CreateView):
    """Feedback view
        Ajax request
        
        
        :CreateViewm: django view
    """
    
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
                
                message="se registro correctamente "
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
    
    
    

