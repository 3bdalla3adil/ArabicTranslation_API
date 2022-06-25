<<<<<<< HEAD
"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls       import include, path

urlpatterns = [
    path('admin/'  , admin.site.urls),
    # path('apis/v1/', include('arabic_keyword_api.urls')),
    path(''        , include('arabic_keyword_api.urls')),
]
=======
"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls       import include, path

urlpatterns = [
    path('admin/'  , admin.site.urls),
<<<<<<< HEAD
    # path('apis/v1/', include('arabic_keyword_api.urls')),
    path(''        , include('arabic_keyword_api.urls')),
=======
    # path(""        ,    ),
    path('apis/v1/', include('arabic_keyword_api.urls')),
>>>>>>> 8771cc18b1ab13e02f90578b7ddef2b7fc253895
]
>>>>>>> 58b842debb869a8e4a5b13211341285f3a15ad95
