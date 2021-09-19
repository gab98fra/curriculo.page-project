import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.generic import TemplateView, View
from dashboard.models import(DatosPersonalesModel, DatosContactoModel, ObjetivoProfesionalModel,
                    ExperienciaProfesionalModel, FormacionAcademicaModel, IdiomasModel, CursosCertificacionesModel)
from profile.mixins import Autenticar_ValidarDatosMixin



class PerfilView(Autenticar_ValidarDatosMixin,View):
    """User profile
    
    
        :Autenticar_ValidarDatosMixin:Validates user authentication
        :View:django view
    """
    template_name="profile/perfil.html"
    
    def get_queryset(self,user):
        "Get user data"
        
        datosPersonales=DatosPersonalesModel.objects.get(user=request.user)
        datosContacto=DatosContactoModel.objects.get(user=request.user)
        objetivoProfesional=ObjetivoProfesionalModel.objects.get(user=request.user)
        experienciaProfesional=ExperienciaProfesionalModel.objects.filter(user=request.user)
        experienciaProfesional=experienciaProfesional.order_by("-is_active", "-start_date")
        formacionAcademica=FormacionAcademicaModel.objects.filter(user=request.user)
        formacionAcademica=formacionAcademica.order_by("-is_active", "-start_date")
        cursos=CursosCertificacionesModel.objects.filter(user=request.user)
        cursos=cursos.order_by("-is_active", "-start_date")
        idiomas=IdiomasModel.objects.filter(user=request.user)
        #Age
        age=(datetime.date.today() - datosPersonales.date_of_birth)/365
        age=age.days
        
        context_data={"datosPersonales":datosPersonales, 
                                                "objetivoProfesional":objetivoProfesional,
                                                "datosContacto":datosContacto,
                                                "formacionAcademica":formacionAcademica,
                                                "experienciaProfesional":experienciaProfesional,
                                                "idiomas":idiomas,
                                                "cursos":cursos,
                                                "edad":age,
                                                }
        return context_data
      
    def get(self, request, *args, **kwargs):

        context_data=self.get_queryset(request.user)  

        return render(request, self.template_name, context_data )
        
