from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('account.urls')),
    path('profile/', include('profile.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('support/', include('app.support.urls')),
]


"Para desarrollo"
from django.conf import settings
from django.conf.urls.static import static

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
