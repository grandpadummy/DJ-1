from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    # path("", views.hello_world, name="hello_world"),
    # path("healthz/", views.healthz_view, name="healthz"),
]

