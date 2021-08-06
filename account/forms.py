from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm, PasswordResetForm, PasswordChangeForm, 
                                        SetPasswordForm, UserChangeForm, ReadOnlyPasswordHashField)
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    "Formulario Iniciar sesión"
    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='Ingrese su USUARIO'
        self.fields['password'].widget.attrs['class']='form-control'
        self.fields['password'].widget.attrs['placeholder']='Password'

        self.error_messages={
        'invalid_login': (
            "Ingrese un %(username)s y password registrado en nuestra plataforma. Considere que "
            "ambos campos son sensibles al uso de mayúsculas."
        ),
        'inactive': ("Está cuenta está inactiva."),
    }

class CreateUserForm(UserCreationForm):
    "Formulario Registrarse"

    def __init__(self,*args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class']='form-control'
        self.fields['first_name'].widget.attrs['placeholder']='Ingrese su nombre'
        self.fields['first_name'].widget.attrs['required']=True
        self.fields['last_name'].widget.attrs['class']='form-control'
        self.fields['last_name'].widget.attrs['placeholder']='Ingrese sus apellidos'
        self.fields['last_name'].widget.attrs['required']=True
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='Ingrese un usuario al menos 8 caracteres alfanúmericos'
        self.fields['email'].widget.attrs['class']='form-control'
        self.fields['email'].widget.attrs['placeholder']='Email'
        self.fields['email'].widget.attrs['required']=True
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['placeholder']='Password al menos 8 caracteres alfanúmericos'
        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['placeholder']='Repeat Password'
        
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username','email' ,'password1','password2']
    
    
class UserDataUpdateForm(forms.ModelForm):
    """ Formulario: Actualizar datos del usuario
    """
    class Meta:
        model=User
        fields = ['first_name','last_name', 'email']


class PasswordChangeForm1(PasswordChangeForm):
#Modificar el password 

    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm1, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['class']='form-control'
        self.fields['old_password'].widget.attrs['placeholder']='Contraseña actual'
        self.fields['new_password1'].widget.attrs['class']='form-control'
        self.fields['new_password1'].widget.attrs['placeholder']='Nueva contraseña'
        self.fields['new_password2'].widget.attrs['class']='form-control'
        self.fields['new_password2'].widget.attrs['placeholder']='Repetir contraseña'



class PasswordResetForm1(PasswordResetForm):
#Recuperar acceso
    
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm1, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class']='form-control'
        self.fields['email'].widget.attrs['placeholder']='Email'
    
    class Meta:
        model = User
        fields = ['email']

class SetPasswordForm1(SetPasswordForm):
#Nodificar la contraseña
    def __init__(self, *args, **kwargs):
        super(SetPasswordForm1, self).__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs['class']='form-control'
        self.fields['new_password1'].widget.attrs['placeholder']='Nueva contraseña'
        self.fields['new_password2'].widget.attrs['class']='form-control'
        self.fields['new_password2'].widget.attrs['placeholder']='Repetir contraseña'


