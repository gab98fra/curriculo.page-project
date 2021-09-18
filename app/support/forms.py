from django import forms
from .models import AssistanceModel, FeedbackModel


class AssistanceForm(forms.ModelForm):
    "Assitance Form"

    class Meta:
        model=AssistanceModel
        fields="__all__"
        exclude=['status']

        labels={
        "issue":"Asunto",
        "description":"Descripción",
        }

class FeedbackForm(forms.ModelForm):
    "Feedback form"
    
    class Meta:
        model=FeedbackModel
        fields="__all__"
        exclude=['user']
        labels={
        "issue":"Asunto",
        "description":"Descripción"
        }
