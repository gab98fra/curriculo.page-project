from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View
from .forms import (DatosPersonalesForm, DatosContactoForm, ExperienciaProfesionalForm, 
                    ObjetivoProfesionalForm,FormacionAcademicaForm, IdiomasForm, CursosCertificacionesForm, CvFileForm)
from .models import (DatosPersonalesModel, DatosContactoModel, ExperienciaProfesionalModel, ObjetivoProfesionalModel,
                     FormacionAcademicaModel, IdiomasModel, CursosCertificacionesModel,CvFileModel )
from profile.permissions import cvFilePermission
from profile.mixins import CvFilePermissionMixin


class DashboardView(TemplateView):
    """Dashboard principal
        -Se obtiene imagen del usuario
        -En caso de no tenerlo se envia por defecto, validación desde el template
    """
    model=DatosPersonalesModel
    template_name="dashboard/dashboard.html"

    def get(self, request, *args, **kwargs):
        try:
            data_user=self.model.objects.get(user=request.user)
            image=data_user.image
            return render(request, self.template_name, {"image": image})
        except:
            image=False
            return render(request, self.template_name, {"image":image})
    

class DatosPersonalesView(TemplateView):
    """Datos personales con las siguiente funciones:
        -GET se valida si tiene datos ya registrados-
            -En caso de contar se manda los datos como contexto y se mustra en el template
            -En cao de no tener registro, se redirecciona hacia la clase DatosPersonalesCreateView

    """

    model=DatosPersonalesModel
    template_name="dashboard/datos_personales/template.html"
    
    def get(self, request, *args, **kwargs):
        data_user=self.model.objects.filter(user=request.user)
        if data_user:
            return render(request, self.template_name, {"data_user":data_user})
        else:
            return redirect("datos_personales_agregar")

class DatosPersonalesCreateView(CreateView):
    """Permite agregar datos personales
        form_valid: obtiene el user logeado, no es enviado desde el formulario
    
    """

    model=DatosPersonalesModel
    form_class=DatosPersonalesForm
    template_name='dashboard/datos_personales/create.html'
    context_object_name="form"
    success_url=reverse_lazy("datos_personales")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DatosPersonalesUpdateView(UpdateView):
    "Actualización de datos personales"

    model=DatosPersonalesModel
    form_class=DatosPersonalesForm
    template_name="dashboard/datos_personales/update.html"
    context_object_name="form"
    success_url=reverse_lazy("datos_personales")


class DatosContactoView(View):
    """Datos de contacto con las siguiente funciones:
        -GET: se valida si tiene datos ya registrados
            -En caso de contar se manda los datos como contexto y se mustra en el template
            -En cao de no tener registro, se redirecciona hacia la clase DatosPersonalesCreateView

    """
    model=DatosContactoModel
    template_name="dashboard/datos_contacto/template.html"
    
    def get(self, request, *args, **kwargs):
        data_user=self.model.objects.filter(user=request.user)
        if data_user:
            return render(request, self.template_name, {"data_user":data_user})
        else:
            return redirect("datos_contacto_agregar")

class DatosContactoCreateView(CreateView):
    """Permite agregar datos de contacto
        form_valid: obtiene el user logeado, no es enviado desde el formulario
    
    """
    model=DatosContactoModel
    form_class=DatosContactoForm
    template_name='dashboard/datos_contacto/create.html'
    context_object_name="form"
    success_url=reverse_lazy("datos_contacto")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DatosContactoUpdateView(UpdateView):
    "Actualización de datos de contacto"

    model=DatosContactoModel
    form_class=DatosContactoForm
    template_name="dashboard/datos_contacto/update.html"
    context_object_name="form"
    success_url=reverse_lazy("datos_contacto")


class ObjetivosView(View):
    """Con las siguiente funciones:
        -GET se valida si tiene datos ya registrados-
            -En caso de contar se manda los datos como contexto y se mustra en el template
            -En cao de no tener registro, se redirecciona hacia la clase ObjetivosCreateView

    """

    model=ObjetivoProfesionalModel
    template_name="dashboard/objetivo_profesional/template.html"
    
    def get(self, request, *args, **kwargs):
        data_user=self.model.objects.filter(user=request.user)
        if data_user:
            return render(request, self.template_name, {"data_user":data_user})
        else:
            return redirect("objetivos_agregar")


class ObjetivosCreateView(TemplateView):
    "Permite crear Objetivos Profesionales y asignar permisos"

    model=ObjetivoProfesionalModel
    template_name='dashboard/objetivo_profesional/create.html'
    success_url=reverse_lazy("objetivos")

    def post(self, request, *args, **kwargs):
        "Obtenemos los datos a través de los atributos html"
        employment=request.POST.get("employment")
        salary=request.POST.get("salary")
        divisa=request.POST.get("divisa")
        objective=request.POST.get("objective")
        objetivoProfesional1=self.model(employment=employment, salary=salary, divisa=divisa, 
                                objective=objective,user=request.user)                        
        objetivoProfesional1.save()
        
        #Asignar permisos, al modelo CvFileModel: llamando la función definida
        cvFilePermission(request.user, CvFileModel)
        
        return HttpResponseRedirect(self.success_url)


class ObjetivosUpdateView(UpdateView):
    "Actualización Objetivos Profesionales"

    model=ObjetivoProfesionalModel
    form_class=ObjetivoProfesionalForm
    template_name="dashboard/objetivo_profesional/update.html"
    context_object_name="form"
    success_url=reverse_lazy("objetivos")


class ExperienciaProfesionalView(TemplateView):
    """Template principal: Experiencia profesional:
        -En caso de contar con información registrada se manda los datos como contexto y se muestra en el template
        -En cao de no tener registro, se redirecciona hacia la clase ExperienciaProfesionalCreateView

    """

    model=ExperienciaProfesionalModel
    template_name="dashboard/experiencia_profesional/template.html"
    
    def get(self, request, *args, **kwargs):
        "Filtrado por trabajos activos y descendentes"

        data_user=self.model.objects.filter(user=request.user)
        data_user=data_user.order_by("-is_active", "-start_date")# - DES
        #data_user=self.model.objects.order_by("-is_active", "-start_date")
        if data_user:
            return render(request, self.template_name, {"data_user":data_user})
        else:
            return redirect("experiencia_profesional_agregar")
            

class ExperienciaProfesionalUpdateView(UpdateView):
    "Actualización de experiencia profesional"

    model=ExperienciaProfesionalModel
    form_class=ExperienciaProfesionalForm
    template_name="dashboard/experiencia_profesional/update.html"
    context_object_name="form"
    success_url=reverse_lazy("experiencia_profesional")

class ExperienciaProfesionalCreateView(CreateView):
    "Permite ir agregando experiencias profesionales"

    model=ExperienciaProfesionalModel
    form_class=ExperienciaProfesionalForm
    template_name='dashboard/experiencia_profesional/create.html'
    context_object_name="form"
    success_url=reverse_lazy("experiencia_profesional")

    def form_valid(self, form):
        "Obtenemos el user, no se envía en el formulario"
        form.instance.user = self.request.user
        return super().form_valid(form)

class ExperienciaProfesionaDeleteView(DeleteView):
    "Elimina expencias profesionales"
    model=ExperienciaProfesionalModel
    context_object_name="form"
    template_name='dashboard/experiencia_profesional/delete.html'
    success_url=reverse_lazy("experiencia_profesional")


class FormacionAcademicaView(View):
    """Templete principal: Formación académica
        -En caso de contar con información registrada se manda los datos como contexto y se muestra en el template
        -En cao de no tener registro, se redirecciona hacia la clase FormacionAcademicaCreateView
    """

    model=FormacionAcademicaModel
    template_name="dashboard/formacion_academica/template.html"
    
    def get(self, request, *args, **kwargs):
        data_user=self.model.objects.filter(user=request.user)
        if data_user:
            return render(request, self.template_name, {"data_user":data_user})
        else:
            return redirect("formacion_academica_agregar")
            

class FormacionAcademicaUpdateView(UpdateView):
    "Actualización Formación académica"

    model=FormacionAcademicaModel
    form_class=FormacionAcademicaForm
    template_name="dashboard/formacion_academica/create.html"
    context_object_name="form"
    success_url=reverse_lazy("formacion_academica")

class FormacionAcademicaCreateView(CreateView):
    "Agrega formación académica"

    model=FormacionAcademicaModel
    form_class=FormacionAcademicaForm
    template_name='dashboard/formacion_academica/create.html'
    context_object_name="form"
    success_url=reverse_lazy("formacion_academica")

    def form_valid(self, form):
        "Obtenemos el user, no se envía en el formulario"
        form.instance.user = self.request.user
        return super().form_valid(form)

class FormacionAcademicaDeleteView(DeleteView):
    "Elimina formación académica"

    model=FormacionAcademicaModel
    context_object_name="form"
    template_name='dashboard/formacion_academica/delete.html'
    success_url=reverse_lazy("formacion_academica")

class IdiomasView(View):
    """Template principal: Idiomas
        -En caso de contar con información registrada se manda los datos como contexto y se muestra en el template
        -En cao de no tener registro, se redirecciona hacia la clase IdiomasCreateView
    """

    model=IdiomasModel
    template_name="dashboard/idiomas/template.html"
    
    def get(self, request, *args, **kwargs):
        data_user=self.model.objects.filter(user=request.user)
        if data_user:
            return render(request, self.template_name, {"data_user":data_user})
        else:
            return redirect("idiomas_agregar")
            

class IdiomasUpdateView(UpdateView):
    "Actualización Idiomas"

    model=IdiomasModel
    form_class=IdiomasForm
    template_name="dashboard/idiomas/create.html"
    context_object_name="form"
    success_url=reverse_lazy("idiomas")

class IdiomasCreateView(CreateView):
    "Agregar Idiomas"

    model=IdiomasModel
    form_class=IdiomasForm
    template_name='dashboard/idiomas/create.html'
    context_object_name="form"
    success_url=reverse_lazy("idiomas")

    def form_valid(self, form):
        "Obtenemos el user, no se envía en el formulario"
        form.instance.user = self.request.user
        return super().form_valid(form)

class IdiomasDeleteView(DeleteView):
    "Elimina idioma"

    model=IdiomasModel
    context_object_name="form"
    template_name='dashboard/idiomas/delete.html'
    success_url=reverse_lazy("idiomas")

class CursosView(View):
    """Template principal: Cursos
        -En caso de contar con información registrada se manda los datos como contexto y se muestra en el template
        -En cao de no tener registro, se redirecciona hacia la clase CursosCreateView
    """

    model=CursosCertificacionesModel
    template_name="dashboard/cursos/template.html"
    
    def get(self, request, *args, **kwargs):
        data_user=self.model.objects.filter(user=request.user)
        if data_user:
            return render(request, self.template_name, {"data_user":data_user})
        else:
            return redirect("cursos_agregar")
            

class CursosUpdateView(UpdateView):
    "Actualización Cursos"

    model=CursosCertificacionesModel
    form_class=CursosCertificacionesForm
    template_name="dashboard/cursos/create.html"
    context_object_name="form"
    success_url=reverse_lazy("cursos")

class CursosCreateView(CreateView):
    "Agrega Cursos"

    model=CursosCertificacionesModel
    form_class=CursosCertificacionesForm
    template_name='dashboard/cursos/create.html'
    context_object_name="form"
    success_url=reverse_lazy("cursos")

    def form_valid(self, form):
        "Obtenemos el user, no se envía en el formulario"
        form.instance.user = self.request.user
        return super().form_valid(form)

class CursosDeleteView(DeleteView):
    "Elimina idioma"

    model=CursosCertificacionesModel
    context_object_name="form"
    template_name='dashboard/cursos/delete.html'
    success_url=reverse_lazy("cursos")


class CvFileView(CvFilePermissionMixin, CreateView):
    "CvFilePermissionMixin: clase definida para validar si tiene permisos"

    model=CvFileModel
    form_class=CvFileForm
    template_name='dashboard/create.html'
    context_object_name="form"
    success_url=reverse_lazy("dashboard")