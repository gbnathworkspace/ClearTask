"""
URL configuration for taskhub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# urls.py

from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from cleartask.views import hello_world, insert_task
from cleartask.dbm_test import InsertTestView, GetTestView, GetTestDetailView, DeleteTestView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hello/', hello_world, name='hello_world'),
    path('api/insert_test/', csrf_exempt(InsertTestView.as_view()), name='insert_test'),
    path('api/get_test/', csrf_exempt(GetTestView.as_view()), name='get_test'),
    path('api/get_test/<int:pk>/', csrf_exempt(GetTestDetailView.as_view()), name='get_test_detail'),
    path('api/delete_test/<int:pk>/', csrf_exempt(DeleteTestView.as_view()), name='delete_test'),
    path('api/insert_task/', csrf_exempt(insert_task), name='insert_task'),
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]

# # Add this if Necessary
# from django.conf import settings
# from django.conf.urls import include

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]


# # Add this if Necessory
# from django.conf import settings
# from django.conf.urls import include

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
