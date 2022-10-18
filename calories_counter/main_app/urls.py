from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name="index"),
    path('catalog/', catalog, name='catalog'),
    path('catalog/<int:category_pk>/', detail_view_category, name='detail_view_category'),
    path('catalog/<int:category_pk>/<int:product_pk>/', detail_view_product, name='detail_view_product')
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
