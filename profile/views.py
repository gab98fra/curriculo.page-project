import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.generic import TemplateView, View
from dashboard.models import(DatosPersonalesModel, DatosContactoModel, ObjetivoProfesionalModel,
                    ExperienciaProfesionalModel, FormacionAcademicaModel, IdiomasModel, CursosCertificacionesModel)
from .utils import render_to_pdf
from .mixins import Autenticar_ValidarDatosMixin



class PerfilView(Autenticar_ValidarDatosMixin,View):
    """Página principal
        -Obtiene la información del usuario logeado
        Notas:
            -get: para un solo registro exitentente en la tabla
            -filter: para varios registro existentes en una tabla
    """
    template_name="profile/perfil.html"

    def get(self, request, *args, **kwargs):
        "Ordenado de manera descente por: activos y fecha de inicio"

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
        #Calcular la edad
        age=(datetime.date.today() - datosPersonales.date_of_birth)/365
        age=age.days

        return render(request, self.template_name, {"datosPersonales":datosPersonales, 
                                                "objetivoProfesional":objetivoProfesional,
                                                "datosContacto":datosContacto,
                                                "formacionAcademica":formacionAcademica,
                                                "experienciaProfesional":experienciaProfesional,
                                                "idiomas":idiomas,
                                                "cursos":cursos,
                                                "edad":age,
                                                })
        
