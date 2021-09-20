from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View
from profile.permissions import cvFilePermission
from profile.mixins import CvFilePermissionMixin
from dashboard.forms import (DatosPersonalesForm, DatosContactoForm, ExperienciaProfesionalForm, 
                    ObjetivoProfesionalForm,FormacionAcademicaForm, IdiomasForm, CursosCertificacionesForm, CvFileForm)
from dashboard.models import (DatosPersonalesModel, DatosContactoModel, ExperienciaProfesionalModel, ObjetivoProfesionalModel,
                     FormacionAcademicaModel, IdiomasModel, CursosCertificacionesModel,CvFileModel )


class DashboardView(TemplateView):
    """Main Dashboard
        
        
        :TemplateView: django view
    """
    model=DatosPersonalesModel
    template_name="dashboard/dashboard.html"

    def get(self, request, *args, **kwargs):
        
        try:
            data_user=self.model.objects.get(user=request.user)
            image=data_user.image
            
        except:
            
            image=False
        
        return render(request, self.template_name, {"image":image})
    

class DatosPersonalesView(TemplateView):
    "User data"

    model=DatosPersonalesModel
    template_name="dashboard/datos_personales/template.html"
    
    def get(self, request, *args, **kwargs):
        
        data_user=self.model.objects.filter(user=request.user)
        
        if data_user:
          
            return render(request, self.template_name, {"data_user":data_user})
        else:
          
            return redirect("datos_personales_agregar")

class DatosPersonalesCreateView(CreateView):
    """User data
        
        
        :CreateView: django view allows create user
    """

    model=DatosPersonalesModel
    form_class=DatosPersonalesForm
    template_name='dashboard/datos_personales/create.html'
    context_object_name="form"
    success_url=reverse_lazy("datos_personales")

    def form_valid(self, form):
        "get user"
        
        form.instance.user = self.request.user
        
        return super().form_valid(form)


class DatosPersonalesUpdateView(UpdateView):
    """Update user data
        
        
        :UpdateView:django view
    """

    model=DatosPersonalesModel
    form_class=DatosPersonalesForm
    template_name="dashboard/datos_personales/update.html"
    context_object_name="form"
    success_url=reverse_lazy("datos_personales")


class DatosContactoView(View):
    """User data
        
        
        :View:django view
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
    
    model=DatosContactoModel
    form_class=DatosContactoForm
    template_name='dashboard/datos_contacto/create.html'
    context_object_name="form"
    success_url=reverse_lazy("datos_contacto")

    def form_valid(self, form):
        "get user"
        
        form.instance.user = self.request.user
        return super().form_valid(form)


class DatosContactoUpdateView(UpdateView):
    "Update data"

    model=DatosContactoModel
    form_class=DatosContactoForm
    template_name="dashboard/datos_contacto/update.html"
    context_object_name="form"
    success_url=reverse_lazy("datos_contacto")


class ObjetivosView(View):
    
    model=ObjetivoProfesionalModel
    template_name="dashboard/objetivo_profesional/template.html"
    
    def get(self, request, *args, **kwargs):
        
        data_user=self.model.objects.filter(user=request.user)
        if data_user:
          
            return render(request, self.template_name, {"data_user":data_user})
        else:
          
            return redirect("objetivos_agregar")


class ObjetivosCreateView(TemplateView):
    "Create data"

    model=ObjetivoProfesionalModel
    template_name='dashboard/objetivo_profesional/create.html'
    success_url=reverse_lazy("objetivos")

    def post(self, request, *args, **kwargs):
        "get data user"
        
        employment=request.POST.get("employment")
        salary=request.POST.get("salary")
        divisa=request.POST.get("divisa")
        objective=request.POST.get("objective")
        objetivoProfesional1=self.model(employment=employment, salary=salary, divisa=divisa, 
                                objective=objective,user=request.user)                        
        objetivoProfesional1.save()
        
        # Set permissions
        cvFilePermission(request.user, CvFileModel)
        
        return HttpResponseRedirect(self.success_url)


class ObjetivosUpdateView(UpdateView):
    

    model=ObjetivoProfesionalModel
    form_class=ObjetivoProfesionalForm
    template_name="dashboard/objetivo_profesional/update.html"
    context_object_name="form"
    success_url=reverse_lazy("objetivos")


class ExperienciaProfesionalView(TemplateView):
    

    model=ExperienciaProfesionalModel
    template_name="dashboard/experiencia_profesional/template.html"
    
    def get(self, request, *args, **kwargs):
        
        data_user=self.model.objects.filter(user=request.user)
        data_user=data_user.order_by("-is_active", "-start_date")# - DES
       
        if data_user:
          
            return render(request, self.template_name, {"data_user":data_user})
        else:
          
            return redirect("experiencia_profesional_agregar")
            

class ExperienciaProfesionalUpdateView(UpdateView):
    "Update data"

    model=ExperienciaProfesionalModel
    form_class=ExperienciaProfesionalForm
    template_name="dashboard/experiencia_profesional/update.html"
    context_object_name="form"
    success_url=reverse_lazy("experiencia_profesional")

class ExperienciaProfesionalCreateView(CreateView):
    "create data"

    model=ExperienciaProfesionalModel
    form_class=ExperienciaProfesionalForm
    template_name='dashboard/experiencia_profesional/create.html'
    context_object_name="form"
    success_url=reverse_lazy("experiencia_profesional")

    def form_valid(self, form):
        "get user"
        
        form.instance.user = self.request.user
        
        return super().form_valid(form)

class ExperienciaProfesionaDeleteView(DeleteView):
    "delete data"
    
    model=ExperienciaProfesionalModel
    context_object_name="form"
    template_name='dashboard/experiencia_profesional/delete.html'
    success_url=reverse_lazy("experiencia_profesional")


class FormacionAcademicaView(View):
   

    model=FormacionAcademicaModel
    template_name="dashboard/formacion_academica/template.html"
    
    def get(self, request, *args, **kwargs):
        
        data_user=self.model.objects.filter(user=request.user)
        if data_user:
          
            return render(request, self.template_name, {"data_user":data_user})
          
        else:
          
            return redirect("formacion_academica_agregar")
            

class FormacionAcademicaUpdateView(UpdateView):
   

    model=FormacionAcademicaModel
    form_class=FormacionAcademicaForm
    template_name="dashboard/formacion_academica/create.html"
    context_object_name="form"
    success_url=reverse_lazy("formacion_academica")

class FormacionAcademicaCreateView(CreateView):
    

    model=FormacionAcademicaModel
    form_class=FormacionAcademicaForm
    template_name='dashboard/formacion_academica/create.html'
    context_object_name="form"
    success_url=reverse_lazy("formacion_academica")

    def form_valid(self, form):
      
        form.instance.user = self.request.user
        return super().form_valid(form)

class FormacionAcademicaDeleteView(DeleteView):
    

    model=FormacionAcademicaModel
    context_object_name="form"
    template_name='dashboard/formacion_academica/delete.html'
    success_url=reverse_lazy("formacion_academica")

class IdiomasView(View):
    
    model=IdiomasModel
    template_name="dashboard/idiomas/template.html"
    
    def get(self, request, *args, **kwargs):
        
        data_user=self.model.objects.filter(user=request.user)
        
        if data_user:
          
            return render(request, self.template_name, {"data_user":data_user})
        else:
          
            return redirect("idiomas_agregar")
            

class IdiomasUpdateView(UpdateView):
    

    model=IdiomasModel
    form_class=IdiomasForm
    template_name="dashboard/idiomas/create.html"
    context_object_name="form"
    success_url=reverse_lazy("idiomas")

class IdiomasCreateView(CreateView):
    

    model=IdiomasModel
    form_class=IdiomasForm
    template_name='dashboard/idiomas/create.html'
    context_object_name="form"
    success_url=reverse_lazy("idiomas")

    def form_valid(self, form):
        
        form.instance.user = self.request.user
        return super().form_valid(form)

class IdiomasDeleteView(DeleteView):

    model=IdiomasModel
    context_object_name="form"
    template_name='dashboard/idiomas/delete.html'
    success_url=reverse_lazy("idiomas")

class CursosView(View):
    

    model=CursosCertificacionesModel
    template_name="dashboard/cursos/template.html"
    
    def get(self, request, *args, **kwargs):
        data_user=self.model.objects.filter(user=request.user)
        if data_user:
            return render(request, self.template_name, {"data_user":data_user})
        else:
            return redirect("cursos_agregar")
            

class CursosUpdateView(UpdateView):
    

    model=CursosCertificacionesModel
    form_class=CursosCertificacionesForm
    template_name="dashboard/cursos/create.html"
    context_object_name="form"
    success_url=reverse_lazy("cursos")

class CursosCreateView(CreateView):
    

    model=CursosCertificacionesModel
    form_class=CursosCertificacionesForm
    template_name='dashboard/cursos/create.html'
    context_object_name="form"
    success_url=reverse_lazy("cursos")

    def form_valid(self, form):
        "get user"
        
        form.instance.user = self.request.user
        return super().form_valid(form)

class CursosDeleteView(DeleteView):
    
    model=CursosCertificacionesModel
    context_object_name="form"
    template_name='dashboard/cursos/delete.html'
    success_url=reverse_lazy("cursos")

