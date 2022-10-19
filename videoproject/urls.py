from django.contrib import admin
from django.urls import path, include
from videos import views as video_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', video_views.index, name='index'),
    path('videos/', include('videos.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
