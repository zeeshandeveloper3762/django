"""
URL configuration for sec_project project.

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
from course.views import learn_python, home
from fees.views import fees_1

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home),

    path('python/', learn_python),
    # you can define multiple rout for one view_function like: 
    # path('learn/', views.learn_python),

    # path('django/', views.learn_django),

    # path('javascript/', views.learn_javascript),

    # path('react/', views.learn_react),

    path('fees_1/', fees_1)
]
