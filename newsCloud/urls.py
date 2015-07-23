from django.conf.urls import include, url
from . import views

urlpatterns=[
url(r'^$',views.get_cloud_today, name='home'),
url(r'news_cloud',views.get_cloud_today,name='get_cloud_today'),
url(r'news_cloud/week', views.get_cloud_week, name='get_cloud_week'),
url(r'news_cloud/month', views.get_cloud_month, name='get_cloud_month'),
url(r'news_cloud/politic',views.get_cloud_politic, name='get_cloud_politic'),
url(r'news_cloud/politic/week',views.get_cloud_politic_week, name='get_cloud_politic_week'),
url(r'news_cloud/politic/month',views.get_cloud_politic_month, name='get_cloud_politic_month'),
#url(r'news_cloud/finance',views.get_cloud_finance, name='get_cloud_finance'),
#url(r'news_cloud/finance/week',views.get_cloud_finance_week, name='get_cloud_finance_week'),
#url(r'news_cloud/finance/month',views.get_cloud_finance_month, name='get_cloud_finance_month'),
url(r'second',views.get_second_page_get, name='get_second_page_get'),
url(u'^to_sec/(?P<urltag>[\w]+)', views.get_second_page, name='get_second_page'),
]

