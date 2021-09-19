from django.shortcuts import redirect
from django.contrib import messages
from django.urls.base import reverse_lazy
from dashboard.models import DatosPersonalesModel, DatosContactoModel, ObjetivoProfesionalModel

class Autenticar_ValidarDatosMixin(object):
    "Authenticated Mixin"
    
    def dispatch(self, request, *args, **kwargs):
        
        if request.user.is_authenticated:
            if (DatosPersonalesModel.objects.filter(user=request.user) and 
                DatosContactoModel.objects.filter(user=request.user) and 
                ObjetivoProfesionalModel.objects.filter(user=request.user)):
                
                return super().dispatch(request, *args, **kwargs)
            else:
                messages.error(request, 'Debe ingresar Datos Personales, Datos de contacto y Objetivos Profesionales')
                messages.error(request, ' - En la barra lateral puede capturar los datos')
                return redirect("datos_personales")
        
        return redirect('dashboard')


class CvFilePermissionMixin(object):
    "Permission Mixin"
    
    permission_required = ('dashboard.view_cvfilemodel', 'dashboard.change_cvfilemodel',
                           'dashboard.delete_cvfilemodel','dashboard.add_cvfilemodel')
    
    url_redirect=None

    def get_perms(self):
        if isinstance(self.permission_required,str):
            return (self.permission_required)
        else:
            return self.permission_required
    
    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy("dashboard")
        
        return self.url_redirect

    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perms(self.get_perms()):
            return super().dispatch(request, *args, **kwargs)
        
        return redirect(self.get_url_redirect())


