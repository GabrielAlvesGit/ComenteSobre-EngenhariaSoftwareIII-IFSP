from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comente-sobre/', include('comente_sobres.urls')),
]
