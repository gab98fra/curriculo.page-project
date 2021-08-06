from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from home.views import Error404View, Error500View


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('account.urls')),
    path('profile/', include('profile.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('support/', include('app.support.urls')),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    
handler404 = Error404View.as_view()
handler500 = Error500View.as_error_view()
