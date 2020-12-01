"""bug_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from tracker_app import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('login/', views.login_view, name='loginpage'),
    path('logout/', views.logout_view, name='logoutpage'),
    path('tickets/add/', views.create_ticket, name='createtick'),
    path('edit/<int:ticket_id>/', views.edit_ticket, name='edittick'),
    path('tickets/<int:user_filed_id>/', views.ticket_detail,
         name='ticket_detail'),
    path('assignperson/<int:ticket_id>/', views.status_view, name='statusview'),
    path('admin/', admin.site.urls),
]
