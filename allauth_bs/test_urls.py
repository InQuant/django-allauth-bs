from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from example import views as example_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', example_views.helloworld),
]