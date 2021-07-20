from django import forms
from django.forms.widgets import Input, Textarea
from django.utils.translation import gettext_lazy as _
from .models import (DatosPersonalesModel, DatosContactoModel, ExperienciaProfesionalModel, ObjetivoProfesionalModel,
                     FormacionAcademicaModel, IdiomasModel, CursosCertificacionesModel,   
                      CvFileModel )

class DatosPersonalesForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DatosPersonalesForm, self).__init__(*args, **kwargs)
        self.fields['other'].widget.attrs['class']='form-control'
        self.fields['other'].widget.attrs['placeholder']='Máx 200 caracteres'
    

    class Meta:
        model=DatosPersonalesModel
        #fields=['date_of_birth', "image", "sex", "relocate", "country", "zip_code", "state", "city", "town", "other"]
        fields="__all__"
        exclude=['user']
        
        labels={
            'date_of_birth':"Fecha de nacimiento",
            'image':"Foto de perfil",
            'sex':"Genero",
            'relocate':"Disponibilidad para reubicarse",
            'country':"País",
            'zip_code':"Código postal",
            'state':"Estado",
            'city':"Ciudad",
            'town':"Alcadía o municipio",
            'other':_("Información adicional")
        }
        
        widgets = {
            'date_of_birth': Input(
                attrs={
                    'type':'date',
                    "required":True
                }
            )
        }

        error_messages = {
            'zip_code': {
                'max_length': ("La longitud no debe superar los 10"),
            
            },
        }



class DatosContactoForm(forms.ModelForm):

    class Meta:
        model=DatosContactoModel
        fields="__all__"
        exclude=['user']
        labels={
            'telephone':"Teléfono",
            'cellphone':"Celular",
            'facebook_social_url':"Facebook",
            'twitter_social_url':"Twitter",
            'instragram_socila_url':"Instagram",
        }
    
class ObjetivoProfesionalForm(forms.ModelForm):
    
    class Meta:
        model=ObjetivoProfesionalModel
        fields="__all__"
        exclude=['user']
        labels={
            'employment':"Puesto deseado",
            'salary':"Sueldo deseado",
            'objective':"Objetivos profesionales",
        }
    
        widgets = {
            'objective': Textarea(
                attrs={
                    'class':'form-control',
                    "placeholder":"Máximo 200 caracteres"
                }
            )
        }


class ExperienciaProfesionalForm(forms.ModelForm):

    class Meta:
        model=ExperienciaProfesionalModel
        fields="__all__"
        exclude=['user']

        labels={
            'employment':"Posición laboral",
            'company':"Empresa",
            'activities':"Actividades y funciones",
            'start_date':"Fecha de inicio",
            'departure_date':"Fecha de finalización",
            'is_active':"Sigo trabajando",
        }

        widgets = {
            'start_date': Input(attrs={'type':'date'}),
            'departure_date': Input(attrs={'type':'date'}),
            'activities': Textarea (
                attrs={
                    'class':'form-control',
                    "placeholder":"Máximo 200 caracteres"
                }
            )
        }


class FormacionAcademicaForm(forms.ModelForm):

    class Meta:
        model=FormacionAcademicaModel
        fields="__all__"
        exclude=['user']
        labels={
            'education_level':"Grado de estudio",
            'college':"Nombre de la institución",
            'career':"Carrera",
            'start_date':"Fecha de inicio",
            'departure_date':"Fecha de finalización",
            'is_active':"Sigo estudiando",
        }

        widgets = {
            'start_date': Input(attrs={'type':'date'}),
            'departure_date': Input(attrs={'type':'date'})
        }

class IdiomasForm(forms.ModelForm):

    class Meta:
        model=IdiomasModel
        fields="__all__"
        exclude=['user']
        labels={
            'language':"Idioma",
            'level':"Nivel",
        }


class CursosCertificacionesForm(forms.ModelForm):

    class Meta:
        model=CursosCertificacionesModel
        fields="__all__"
        exclude=['user']
        labels={
            'course':"Curso o certificación",
            'link':"Enlace",
            'start_date': "Fecha de inicio",
            'departure_date': "Fecha de finalización",
            'is_active':"Sigo estudiando",
            'description':"Descripción",
        }

        widgets = {
            'start_date': Input(attrs={'type':'date'}),
            'departure_date': Input(attrs={'type':'date'})
        }

class CvFileForm(forms.ModelForm):

    class Meta:
        model=CvFileModel
        fields=['name', "file", "user"]
        labels={
            'name':"Nombre",
            'file':"Adjuntar",
        }

        