from django.conf.urls import url
from . import views   






       
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$',views.register),
    url(r'^login$',views.login),
    url(r'^logout$',views.logout),
    url(r'^dashboard$',views.dashboard),
    url(r'^wish_items/create$',views.create),
    url(r'^add_wish$',views.add_wish),
    url(r'^joinwish/(?P<wish_id>\d+)$',views.add_to_mywish_too),
    url(r'^removewish/(?P<wish_id>\d+)$',views.remove_from_mywish),
    url(r'^deletewish/(?P<wish_id>\d+)$',views.delete_from_mywish),
    url(r'^wish_items/(?P<item_id>\d+)$',views.item_wished_by)


]