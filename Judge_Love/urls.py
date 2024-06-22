"""
URL configuration for Judge_Love project.

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
from django.urls import path, include
from accounts.views import login_view, signup_view
from stories.views import story_view, result_view, appeal_view, supreme_appeal_view
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('story/', story_view, name='story'),
    path('result/', result_view, name='result'),
    path('appeal/', appeal_view, name='appeal'),
    path('supreme_appeal/', supreme_appeal_view, name='supreme_appeal'),
    path('', RedirectView.as_view(url='/login/', permanent=True)),
]
