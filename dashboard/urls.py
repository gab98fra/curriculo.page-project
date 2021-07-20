from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import( DashboardView, DatosPersonalesCreateView, DatosPersonalesView, DatosPersonalesUpdateView, 
                    DatosContactoView,DatosContactoCreateView, DatosContactoUpdateView, ExperienciaProfesionalView,
                    ExperienciaProfesionalUpdateView,ExperienciaProfesionalCreateView,ExperienciaProfesionaDeleteView, 
                    ObjetivosView, ObjetivosCreateView, ObjetivosUpdateView, FormacionAcademicaView, 
                    FormacionAcademicaCreateView, FormacionAcademicaUpdateView, FormacionAcademicaDeleteView,
                    IdiomasView, IdiomasCreateView, IdiomasUpdateView, IdiomasDeleteView,CursosView, CursosCreateView,
                    CursosUpdateView, CursosDeleteView, CvFileView )


urlpatterns = [
    path('', login_required(DashboardView.as_view()), name="dashboard"),
    path('datos_personales/', login_required(DatosPersonalesView.as_view()), name="datos_personales"),
    path('datos_personales_agregar/',login_required(DatosPersonalesCreateView.as_view()), 
                                                name="datos_personales_agregar"),
    path('datos_personales_modificacion/<int:pk>', login_required(DatosPersonalesUpdateView.as_view()), 
                                                name="datos_personales_modificacion"),
    path('datos_contacto/',login_required(DatosContactoView.as_view()), name="datos_contacto"),
    path('datos_contacto_agregar/', login_required(DatosContactoCreateView.as_view()), name="datos_contacto_agregar"),
    path('datos_contacto_modificacion/<int:pk>', login_required(DatosContactoUpdateView.as_view()), 
                                                name="datos_contacto_modificacion"),
    path('objetivos/', login_required(ObjetivosView.as_view()), name="objetivos"),
    path('objetivos_agregar/', login_required(ObjetivosCreateView.as_view()), name="objetivos_agregar"),
    path('objetivos_modificacion/<int:pk>', login_required(ObjetivosUpdateView.as_view()), 
                                                name="objetivos_modificacion"),
    path('experiencia_profesional/', login_required(ExperienciaProfesionalView.as_view()), 
                                                name="experiencia_profesional"),
    path('experiencia_profesional_modificacion/<int:pk>', login_required(ExperienciaProfesionalUpdateView.as_view()), 
                                                name="experiencia_profesional_modificacion"),
    path('experiencia_profesional_agregar/', login_required(ExperienciaProfesionalCreateView.as_view()), 
                                                name="experiencia_profesional_agregar"),    
    path('experiencia_profesional_eliminar/<int:pk>', login_required(ExperienciaProfesionaDeleteView.as_view()), 
                                                name="experiencia_profesional_eliminar"),                                                
    path('formacion_academica/', login_required(FormacionAcademicaView.as_view()), name="formacion_academica"),
    path('formacion_academica_modificacion/<int:pk>', login_required(FormacionAcademicaUpdateView.as_view()), 
                                                name="formacion_academica_modificacion"),
    path('formacion_academica_agregar/',login_required(FormacionAcademicaCreateView.as_view()), 
                                                name="formacion_academica_agregar"),    
    path('formacion_academica_eliminar/<int:pk>', login_required(FormacionAcademicaDeleteView.as_view()), 
                                                name="formacion_academica_eliminar"),                                                                                        
    path('idiomas/', login_required(IdiomasView.as_view()), name="idiomas"),
    path('idiomas_modificacion/<int:pk>', login_required(IdiomasUpdateView.as_view()), name="idiomas_modificacion"),
    path('idiomas_agregar/', login_required(IdiomasCreateView.as_view()), name="idiomas_agregar"),    
    path('idiomas_eliminar/<int:pk>', login_required(IdiomasDeleteView.as_view()), name="idiomas_eliminar"),
    path('cursos/',login_required(CursosView.as_view()), name="cursos"),
    path('cursos_modificacion/<int:pk>', login_required(CursosUpdateView.as_view()), name="cursos_modificacion"),
    path('cursos_agregar/', login_required(CursosCreateView.as_view()), name="cursos_agregar"),    
    path('cursos_eliminar/<int:pk>', login_required(CursosDeleteView.as_view()), name="cursos_eliminar"),
    path('cv', login_required(CvFileView.as_view()), name="cv"),
]



