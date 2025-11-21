from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # userpage app routes
    path('user-page/', include('userpage.urls')),
]
