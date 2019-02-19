"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from django.urls import url, include                 # add this
from rest_framework import routers                    # add this
from bitstariff import views                            # add this

router = routers.DefaultRouter()                      # add this
router.register(r'todos', views.TodoView, 'todo') 

urlpatterns = [
    url('admin/', admin.site.urls),         
    url('api/', include(router.urls)),              
    url(r'^li/', include("li.urls"))              
]