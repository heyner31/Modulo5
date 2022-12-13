from django.urls import path, include
from services import views
# from .api import ServiceSerializer
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('api/', ServiceSerializer, 'apirest')

Services_urlpatterns = ([
    path('create_pedido/', views.ServiceCreatePedido.as_view(), name='create_pedido'),
    path('success_pedido/', views.PedidoSuccess.as_view(), name='success_pedido'),
    path('detalle_pedido/', views.ver_detalle_pedido, name='detalle_pedido'),
    path('',views.service_list, name='service_list'),
    path('create/',views.create, name='create'),
    path('update/<int:service_id>',views.update, name='update'),
    # path('rest/', include(router.urls)),
], 'services')


