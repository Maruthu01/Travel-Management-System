"""
URL configuration for DBproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from DBapp import views
from django.urls import include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Welcome/',views.Welcome,name='Welcome'),
    path('',views.Register1,name='Register'),
    path('Login_page/',views.Login_page,name='Login_page'),
    path('Login1/',views.Login1,name='Login1'),
    path('Payment/',views.Payment,name='Payment'),
    path('Welcome/About/',views.About,name='About'),
    path('Success/',views.Success,name='Success'),
    path('send/',views.send_whatsapp_message,name='send_message'),
    path('myapp/', include('DBapp.urls')),
    path('Welcome/Bookin/',views.Bookin,name='Bookin'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('add_review/', views.add_review, name='add_review'),
    path('update_review/<int:pk>/', views.update_review, name='update_review'),
    path('delete_review/<int:pk>/', views.delete_review, name='delete_review'),
    path('reviews/', views.list_reviews, name='list_reviews'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 