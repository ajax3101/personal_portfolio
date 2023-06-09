from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('portfolio/', include('portfolio.urls'), name='portfolio'),
    path('blog/', include('blog.urls'), name='blog'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)