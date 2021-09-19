from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import (DatosPersonalesModel, DatosContactoModel, ExperienciaProfesionalModel, ObjetivoProfesionalModel,
                    FormacionAcademicaModel, IdiomasModel, CursosCertificacionesModel,   
                      CvFileModel )


class DatosPersonalesResource(resources.ModelResource):
  "Import & export"

    class Meta:
        model=DatosPersonalesModel

class DatosPersonalesAdmin(ImportExportModelAdmin ,admin.ModelAdmin):

    search_fields=['country']
    list_display=("country", "zip_code","state",)
    readonly_fields=("updated",)
    resource_class=DatosPersonalesResource

class DatosContactoAdmin(admin.ModelAdmin):
    readonly_fields=("modify_date")


admin.site.register(DatosPersonalesModel, DatosPersonalesAdmin)
admin.site.register(DatosContactoModel)
admin.site.register(ObjetivoProfesionalModel)
admin.site.register(ExperienciaProfesionalModel)
admin.site.register(FormacionAcademicaModel)
admin.site.register(IdiomasModel)
admin.site.register(CursosCertificacionesModel)
admin.site.register(CvFileModel)



