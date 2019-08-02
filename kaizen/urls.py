from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from apps.metric import views as metric_views

urlpatterns = [
    url(r'^', metric_views.get, name='metric'),
    path('admin/', admin.site.urls),
]
