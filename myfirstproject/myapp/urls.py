from django.urls import path
from . import views

urlpatterns = [
    path('',views.myfirfun,name = "index"),
    path('add/<int:a>/<int:b>',views.myfirfunadd,name = "add"),
     path('json/<str:name>/<int:age>',views.myfirjson,name = "json"),
]