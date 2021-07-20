from django.urls import path
from .views import PerfilView, PdfFileView

urlpatterns = [
    path('', PerfilView.as_view(), name="perfil"),
    path('file_pdf/', PdfFileView.as_view(), name="file_pdf"),
]

