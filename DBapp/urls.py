from django.urls import path
from .views import send_whatsapp_message
from DBapp import views
from django.views.generic.base import TemplateView 


urlpatterns = [
    path('send/', send_whatsapp_message, name='send_message'),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success'),

]   
