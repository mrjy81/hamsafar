from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from azbankgateways.urls import az_bank_gateways_urls

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('account/', include('account.urls')),
    path('ds/', include('dashboards.urls')),
    path('bankgateways/', az_bank_gateways_urls()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
