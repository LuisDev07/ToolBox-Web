from django.urls import path
from django.conf.urls import handler404, handler500
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('qr-generator/', views.QRgenerator, name='QR'),
    path('passwordseguro/', views.generatorpassword, name='PS'),
    
    
]
handler404 = views.handler404
handler500 = views.handler500