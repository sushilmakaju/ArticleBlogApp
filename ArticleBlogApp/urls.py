from django.urls import path
from django.conf import settings
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('', homeview, name='Articlelist'),
    path('about/', aboutview, name='aboutview'),
    path('createarticle/', createarticle_view, name='createarticle'),
    path('article/<slug>/', article_details, name='article_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

