# calories_counter/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
    # Admin interface URL
    path('admin/', admin.site.urls),
    
    # Include URLs from the main_app application
    path('', include("main_app.urls")),
    
    # Include URLs from the cart application
    path('cart/', include("cart.urls"))
]

# Serve static files during production
if not settings.DEBUG:
    urlpatterns.append(path('static/<path:path>/', serve, {'insecure': True}))
    
# Serve media files during development
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    