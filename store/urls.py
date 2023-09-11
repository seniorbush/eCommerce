from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('basket/', views.basket, name='basket'),
    path('checkout/', views.checkout, name='checkout'),
    path('product/<product_id>/', views.product, name='product'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)