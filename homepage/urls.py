from django.conf.urls import patterns, url

from homepage import views

'''
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^assets', views.assets, name='assets'),
    url(r'^delete_asset/(?P<UIDP>[\w-]+)', views.delete_asset, name='delete_asset'),
    url(r'^delete_location/(?P<UIDP>[\w-]+)', views.delete_location, name='delete_location'),
    url(r'^delete_manufacturer/(?P<UIDP>[\w-]+)', views.delete_manufacturer, name='delete_manufacturer'),
    url(r'^edit_asset/(?P<UIDP>[\w-]+)', views.edit_asset, name='edit_asset'),
    url(r'^edit_location/(?P<UIDP>[\w-]+)', views.edit_location, name='edit_location'),
    url(r'^edit_manufacturer/(?P<UIDP>[\w-]+)', views.edit_manufacturer, name='edit_manufacturer'),
    url(r'^locations', views.locations, name='locations'),
    url(r'^manufacturers', views.manufacturers, name='manufacturers'),
    url(r'^new_asset', views.new_asset, name='new_asset'),
    url(r'^new_location', views.new_location, name='new_location'),
    url(r'^new_manufacturer', views.new_manufacturer, name='new_manufacturer'),
]
'''
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^assets', views.assets, name='assets'),
    url(r'^delete_asset/(?P<UIDP>[\w-]+)', views.delete_asset, name='delete_asset'),
    url(r'^delete_location/(?P<UIDP>[\w-]+)', views.delete_location, name='delete_location'),
    url(r'^delete_manufacturer/(?P<UIDP>[\w-]+)', views.delete_manufacturer, name='delete_manufacturer'),
    url(r'^edit_asset/(?P<UIDP>[\w-]+)', views.edit_asset, name='edit_asset'),
    url(r'^edit_location/(?P<UIDP>[\w-]+)', views.edit_location, name='edit_location'),
    url(r'^edit_manufacturer/(?P<UIDP>[\w-]+)', views.edit_manufacturer, name='edit_manufacturer'),
    url(r'^locations', views.locations, name='locations'),
    url(r'^manufacturers', views.manufacturers, name='manufacturers'),
    url(r'^new_asset', views.new_asset, name='new_asset'),
    url(r'^new_location', views.new_location, name='new_location'),
    url(r'^new_manufacturer', views.new_manufacturer, name='new_manufacturer'),
)