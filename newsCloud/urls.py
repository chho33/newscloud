from django.conf.urls import include, url
from . import views

urlpatterns=[
url(r'^$',views.get_cloud_today, name='home'),
url(r'news_cloud',views.get_cloud_today,name='get_cloud_today'),
url(r'news_cloud/week', views.get_cloud_week, name='get_cloud_week'),
url(r'news_cloud/month', views.get_cloud_month, name='get_cloud_month'),

]
