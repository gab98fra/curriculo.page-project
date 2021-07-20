from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


def cvFilePermission(user, modelo):
    "Agrega permisos al user logeado en el modelo CvFileModel"
    
    content_type = ContentType.objects.get_for_model(modelo)
    
    permission_add = Permission.objects.get(
        codename='add_cvfilemodel',
        name='Can add Archivo',
        content_type=content_type,
    )
    permission_delete = Permission.objects.get(
        codename='delete_cvfilemodel',
        name='Can delete Archivo',
        content_type=content_type,
    )
    permission_change = Permission.objects.get(
        codename='change_cvfilemodel',
        name='Can change Archivo',
        content_type=content_type,
    )
    permission_view = Permission.objects.get(
        codename='view_cvfilemodel',
        name='Can view Archivo',
        content_type=content_type,
    )

    user.user_permissions.add(permission_add, permission_delete, permission_change, permission_view)
    return None
