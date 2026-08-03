from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('dashboard/', admin.site.urls),
    path('accounts/',include("accounts.urls")),
    path('blog/',include("blog.urls")),
    path('',include("core.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)