from django.urls import path
from .views import Register
from .views import LoginView
from .views import UserView
from .views import GetAllUser
from .views import RetrieveUpdateDelete

urlpatterns = [
    path('register/', Register.as_view(), name =''),
    path('login/', LoginView.as_view(), name =''),
    path('user/', UserView.as_view(), name =''),
    path('alluser/', GetAllUser.as_view(), name =''),
    path('RUD/<int:pk>/', RetrieveUpdateDelete.as_view(), name ='RUD'),
]