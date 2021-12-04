"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from HomePage.views import Homepage_view, Contact_view, Project_view, About_view, Elec_project, Prog_project, DYI_project
from projects_app.views import data_detail_view

urlpatterns = [
    path('', Homepage_view, name='home'),
    path('project/elc-design/', Elec_project, name='elec-design'),
    path('project/prg/', Prog_project, name='elec-design'),
    path('project/dyi/', DYI_project, name='elec-design'),
    path('contact/', Contact_view, name='contact'),
    path('project/', Project_view, name='project'),
    path('data/', data_detail_view, name='data'),
    path('about/', About_view, name='about'),
    path('admin/', admin.site.urls),
    
]
