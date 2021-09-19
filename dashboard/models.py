from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    "Photo path"
    
    return 'photo/user_{0}/{1}'.format(instance.user.id, filename)


class DatosPersonalesModel(models.Model):
    
    sex_op=(
        ('Femenino', 'Mujer'),
        ('Masculino', 'Hombre'),
        ('NA', 'No definido'),
    )

    relocate_op=(
        ('Si', 'Reubicarse'),
        ('No', 'No reubicarse'),
    
    )

    id=models.BigAutoField("id", primary_key=True,)
    date_of_birth=models.DateField("date_of_birt", blank=True, null=True)
    image=models.ImageField("image", upload_to=user_directory_path, blank=True, null=True)#upload_to='photo/%y/%m/%d/'
    sex=models.CharField("sex", max_length=12, choices=sex_op, blank=True, null=True)
    relocate=models.CharField('relocate', max_length=2, choices=relocate_op, help_text="Dispuesto a reubicarse")
    country=models.CharField("country", max_length=30, blank=True, null=True)
    zip_code=models.IntegerField("zip_code", blank=True, null=True)
    state=models.CharField(max_length=50,blank=True, null=True)
    city=models.CharField(max_length=50,blank=True, null=True)
    town=models.CharField(max_length=50,blank=True, null=True)
    other=models.TextField(max_length=200, blank=True, null=True, help_text="Otra información, opcional")
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="user")

    class Meta:
        ordering = ["id"]
        verbose_name = "Dato Personal"    
        verbose_name = "Dato Personales"    
    
    def __str__(self):
        return self.city

    def userStatus(self):
        "Retorna si nacio el siglo XX o XXI"
        import datetime
        if self.date_of_birth < datetime.date(1999, 12,31):
            return ("Siglo XX")
        else:
            return "Siglo XXI"


class DatosContactoModel(models.Model):
    
    id=models.AutoField(primary_key=True)
    telephone=models.IntegerField(blank=True, null=True)
    cellphone=models.IntegerField(blank=True, null=True)
    linkedin_social_url=models.URLField(max_length=70, blank=True, default="https://curriculo.page")
    github_social_url=models.URLField(max_length=70, blank=True, default="https://curriculo.page")
    facebook_social_url=models.URLField(max_length=70, blank=True,default="https://curriculo.page")
    twitter_social_url=models.URLField(max_length=70, blank=True, default="https://curriculo.page")
    instagram_social_url=models.URLField(max_length=70, blank=True,default="https://curriculo.page")
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Datos de Contacto"
        ordering = ["id"]

    def __str__(self):
        return str(self.cellphone)


class ObjetivoProfesionalModel(models.Model):
    
    list_divisa=(
        ("MX", "MX"),
        ("USD", "USD"),
    )
    
    id=models.AutoField(primary_key=True)
    employment=models.CharField(max_length=50)
    salary=models.FloatField()
    divisa=models.CharField(max_length=5, choices=list_divisa, blank=True, null=True)
    objective=models.TextField(max_length=200, blank=True, null=True)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name="Objetivo"
        verbose_name_plural = "Objetivos"
        ordering = ["id"]

    def __str__(self):
        return self.employment

class ExperienciaProfesionalModel(models.Model):
    
    id=models.AutoField(primary_key=True)
    employment=models.CharField(max_length=50, blank=False)
    company=models.CharField(max_length=70,  blank=False)
    activities=models.TextField(max_length=200)
    start_date=models.DateField(blank=False)
    departure_date=models.DateField(blank=True, null=True)
    is_active=models.BooleanField(default=False, blank=True)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Experiencia profesional"
        ordering = ["id"]

    def __str__(self):
        return self.employment

class FormacionAcademicaModel(models.Model):
    
    leve_list=(
        ('Primaria','Primaria'),
        ('Secundaria','Secundaria'),
        ('Preparatoria','Preparatoria'),
        ('Licenciatura','Licenciatura'),
        ('Posgrado','Posgrado'),
    )
    id=models.AutoField(primary_key=True)
    educational_level=models.CharField(choices=leve_list, max_length=18, blank=False)
    college=models.CharField(max_length=70, blank=False)
    career=models.CharField(max_length=50, blank=False)
    start_date=models.DateField(blank=False)
    departure_date=models.DateField(blank=False)
    is_active=models.BooleanField(default=False)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Formación académica"
        ordering = ["id"]

    def __str__(self):
        return self.educational_level


class IdiomasModel(models.Model):
    
    language_list=(
        ("Nativo", "Nativo"),
        ("Principiante", "Principiante"),
        ("Intermedio", "Intermedio"),
        ("Avanzado", "Avanzado"),
    )
    id=models.AutoField(primary_key=True)
    language=models.CharField(max_length=25, blank=False)
    level=models.CharField(choices=language_list, max_length=13, blank=False)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Idioma"
        verbose_name_plural = "Idiomas"
        ordering = ["language"]

    def __str__(self):
        return self.language


class CursosCertificacionesModel(models.Model):
    
    id=models.AutoField(primary_key=True)
    course=models.CharField(max_length=50,blank=False )
    college=models.CharField(max_length=50,blank=True, null=True )
    link=models.URLField(max_length=70,blank=True, null=True)
    start_date=models.DateField(blank=True, null=True)
    departure_date=models.DateField(blank=True, null=True)
    is_active=models.BooleanField(default=False)
    description=models.TextField(max_length=50)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["course"]

    def __str__(self):
        return self.course

class CvFileModel(models.Model):
    
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50, blank=False)
    file=models.FileField(upload_to="file/%y/%m/%d/")
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Archivo"

    def __str__(self):
        return self.name
