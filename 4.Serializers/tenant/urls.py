from django.urls import path
from .views import TenantAPIClass
urlpatterns = [
    path('t/', TenantAPIClass.as_view({'get':"list",'post':'create'})),
    path('t/<int:pk>',TenantAPIClass.as_view({'get':'retrieve','put':'update','delete':'destroy','patch':'partial_update'}))
]
