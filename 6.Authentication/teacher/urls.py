from django.urls import path

from .views import TeacherRegistrationAPIView
from rest_framework.authtoken import views
# from  rest_framework_simplejwt.views import(
#     TokenObtainPairView,
#     TokenRefreshView
# )
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import TeacherTokenGenerationAPI

urlpatterns = [
    
    path('registration/',TeacherRegistrationAPIView.as_view(), name='teacher_token'),
    path('teacher-login/',TeacherTokenGenerationAPI.as_view(), name='teacher-login'),

    #CRUD on Teacher and Student
    # path('teacher/', TeacherCRAPI.as_view(), name ='teacher-create-Retrieve'),
    # path('teacher/<int:pk>/', TeacherRUDAPI.as_view(), name= 'teacher-RUD'),
    # path('student/', StudentCRAPI.as_view(), name = 'Student-create-Re'),
    # path('student/<int:pk>/', StudentRUDAPI.as_view(), name='student-RU'),
    
    #Token generations Session 
    # path('api-token-auth/', views.obtain_auth_token, name='token-generator'),
    # path('teacher-registration/',TeacherRegistration.as_view(), name='teacher token')

    # JWT token
    # path('api/token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name= 'token_refresh'),
]