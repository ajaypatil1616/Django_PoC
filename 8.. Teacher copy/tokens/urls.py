from django.urls import path
from .views import TeacherRegistrationAPIView
from .views import TeacherTokenGenerationAPI


urlpatterns = [
    
    path('registration/', TeacherRegistrationAPIView.as_view(),name='teacher-registration'),
    path('login/', TeacherTokenGenerationAPI.as_view(),name='teacher-registration')
]



#custom permissions classes
#Normal JWT  
#cutomize teacher using abstract and base manger and perform CRUD

##POC:
#CRUD on API with authentications and persmissions(custome) throught JWT, BasicAuthecation 
#with validations class based generic API view
# add superuser 