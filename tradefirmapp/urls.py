from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("createorder", views.create_order, name="createorder"),
    path("createclient", views.create_client, name="createclient"),
    path("createitem", views.create_item, name="createitem"),
    path("createdispatch", views.create_dispatch, name="createdispatch"),
    path("createinward", views.create_inward, name="createinward"),
    path("reportorders", views.report_orders, name="reportorders"),
    path("test", views.test, name="test")
]