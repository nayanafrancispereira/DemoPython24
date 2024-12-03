from django.urls import path
from  . import views


app_name= 'shopapp'
urlpatterns = [

    # path('',views.index,name='index')

     path('',views.allProdCart,name='allProdCart'),
     path('home/<slug:c_slug>/', views.allProdCart, name='product_by_category'),
     # path('<slug:c_slug>/',views.allProdCart,name='product_by_category'),
     path('<slug:c_slug>/<slug:product_slug>/',views.ProDetail,name='prodCatDetail'),


]