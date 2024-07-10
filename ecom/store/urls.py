from django.urls import path
from  .import views
urlpatterns = [

    path('',views.main,name='main'),
    path('register/', views.register, name='register'),
    path('logu/', views.logu, name='logu'),
    path('regi/', views.register, name='regi'),
    path('product/', views.product, name='product'),
    path('category/', views.category, name='collections'),

]
