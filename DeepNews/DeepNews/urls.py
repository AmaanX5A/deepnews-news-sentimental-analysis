"""DeepNews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import  url,include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Home.views import  ChartData,get_data
from Home import views

urlpatterns = urlpatterns = [
    url(r'^$',views.HOME,name='index'),
    url(r'^api/chart/data/$', ChartData.as_view()),
    url(r'^api/data/$', get_data, name='api-data'),
    url(r'^index/$', views.index),
    url(r'^LATEST/$', views.LATEST),
    url(r'^WORLD/$', views.WORLD),
    url(r'^BBC/$', views.BBC),
    url(r'^CNN/$', views.CNN),
    url(r'^SKY/$', views.SKY),
    url(r'^HOME/$', views.HOME),
    url(r'^POSITIVE/$', views.POS),
    url(r'^NEGATIVE/$', views.NEG),
    url(r'^NEUTRAL/$', views.NEU),
    url(r'^favicon.ico/$', views.noth),
    url(r'(?P<uuid>[-\w]+)/$', views.single_post, name='single_post'),
    url(r'(?P<pid>[-\w]+)/$', views.records, name='records'),
    url(r'(?P<uid>[-\w]+)/$', views.Pages, name='Pages'),



    url(r'^index/single_post/$', views.single_post),

    url(r'^contact/$', views.contact),
    url(r'^about_us/$', views.about_us),
    path('admin/', admin.site.urls),
    ]
