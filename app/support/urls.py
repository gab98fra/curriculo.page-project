from django.urls import path
from .views import (FAQView, FAQListView, AssistanceView, AssistanceCreateView,AssistanceListView, 
                    AssistanceUpdateView, FeedbackView)

app_name="support"

urlpatterns = [
    
    path('faq/', FAQView.as_view(), name="faq"),
    path('faq_list/', FAQListView.as_view(), name="faq_list"),
    path('assistance/', AssistanceView.as_view(), name="assistance"),
    path('assistance_list/', AssistanceListView.as_view(), name="assistance_list"),
    path('assistance_create/', AssistanceCreateView.as_view(), name="assistance_create"),
    path('assistance_update/<int:pk>', AssistanceUpdateView.as_view(), name="assistance_update"),
    path('feedback/', FeedbackView.as_view(), name="feedback"),#AJAX
    
    ]