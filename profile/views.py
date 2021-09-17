import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.generic import TemplateView, View
from dashboard.models import(DatosPersonalesModel, DatosContactoModel, ObjetivoProfesionalModel,
                    ExperienciaProfesionalModel, FormacionAcademicaModel, IdiomasModel, CursosCertificacionesModel)
from profile.mixins import Autenticar_ValidarDatosMixin



class PerfilView(Autenticar_ValidarDatosMixin,View):
    """Página principal
        Obtiene la información del usuario logeado
        
        :Autenticar_ValidarDatosMixin, mixin creado para autenticación y validación de datos
        :view, clase django
    """
    template_name="profile/perfil.html"
    
    def get_queryset(self,user):
        "Retonara datos del usuario"
        
        datosPersonales=DatosPersonalesModel.objects.get(user=request.user)
        datosContacto=DatosContactoModel.objects.get(user=request.user)
        objetivoProfesional=ObjetivoProfesionalModel.objects.get(user=request.user)
        experienciaProfesional=ExperienciaProfesionalModel.objects.filter(user=request.user)
        experienciaProfesional=experienciaProfesional.order_by("-is_active", "-start_date") # Ordenado de manera descente por: activos y fecha de inicio
        formacionAcademica=FormacionAcademicaModel.objects.filter(user=request.user)
        formacionAcademica=formacionAcademica.order_by("-is_active", "-start_date")
        cursos=CursosCertificacionesModel.objects.filter(user=request.user)
        cursos=cursos.order_by("-is_active", "-start_date")
        idiomas=IdiomasModel.objects.filter(user=request.user)
        #Calcular la edad
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
        "Perfil del usuario"

        context_data=self.get_queryset(request.user)  

        return render(request, self.template_name, context_data )
        
