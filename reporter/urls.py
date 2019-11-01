from django.conf.urls import include,url

#from views import HomePageView, county_datasets,point_datasets
from . import views

urlpatterns = [
	url(r'^$', views.HomePageView.as_view(), name = 'home'),
	url(r'^county_data/$', views.county_datasets, name = 'county'),
	url(r'^incidence_data/$', views.point_datasets, name = 'incidences'),


]
