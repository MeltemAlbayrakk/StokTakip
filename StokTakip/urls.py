
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    # bu kodla stok app icindeki urlsi ana uygulamaya dahil etmis olduk
    path("", include("stok.urls")),
    path("account/", include("account.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
