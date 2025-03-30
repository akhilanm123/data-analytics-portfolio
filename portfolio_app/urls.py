from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('skills/', views.skills, name='skills'),
    path('contact/', views.contact, name='contact'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)





