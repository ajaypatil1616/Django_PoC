from .models import Admin, Employee
from .serializations import EmployeeSerializer,AdminSerializer
from .permissions import IsAdminOrNot,IsValidEmployeeOrNot,HasManagerAccessOrNot,HasManagerItselfAccess
from .authentications import IsEmployeeOrNot
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny
from rest_framework.authentication import BasicAuthentication
from django.contrib.auth import authenticate
from django.conf import settings
import jwt, datetime
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import AccessToken



## ADMIN 
#Register admin
class AdminCreateAPI(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        data['role'] = 'admin'
        serializer = AdminSerializer(data = data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response({"success":"successfully created Admin","data":serializer.data})

#Admin Log In
class AdminLogInAPI(generics.CreateAPIView):
    authentication_classes = [BasicAuthentication]
    
    def post(self, request):        
        username = request.data.get('username')
        password = request.data.get('password')
        if not password or not username:
            return Response("Please Enter username and password correctly  ")

        user = authenticate(request, username = username, password = password)
        if not user:
            return Response("invalid username or password")
        return Response("Log in successfully")


# Admin Dashboard : Details of all the Manager and Employees (combined)
class ListAllManagerAndEmployees(generics.ListAPIView):
    
    authentication_classes = [BasicAuthentication]
    permission_classes =[IsAdminOrNot]  
    serializer_class = AdminSerializer
    
    def get_queryset(self):
        managers = Admin.objects.filter(role ='manager')
        employees = Employee.objects.all()
        managers_data = AdminSerializer(managers, many =True).data
        employees_data = EmployeeSerializer(employees, many = True).data

        all_data = {"managers":managers_data ,"employees": employees_data}
        return all_data
    
    def list(self, request):
        queryset = self.get_queryset()
        return Response(queryset)
     
    
    
## Manager   
#Register Manager by admin
class ManagerCreateAPI(generics.CreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
   
    def create(self, request):
        data = request.data
        data['role']= 'manager'
        serializer = AdminSerializer(data = data)
        
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response({"success":"successfully created Manager","data":serializer.data})
        
#Retrieve, Update and destroy Manager by Admin
class ManagerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    
    def get_queryset(self):
       queryset = super().get_queryset()
       queryset = queryset.filter(role = 'manager')
       return queryset
   
#Log in Manager :Token Generation 
class ManagerLogIn(generics.CreateAPIView):
    permission_classes = [AllowAny] 
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response("You forgot to enter username OR Password or Both")
        user = authenticate(request, username =username, password = password)
        if not user:
            return Response("Invalid credentials")
        
        refresh = RefreshToken.for_user(user)

        return Response({"refresh":str(refresh),
                         "access":str(refresh.access_token),
                         "access expires":refresh.access_token['exp'],
                         })

# Update and View of manager by manager(himself)
class RetrieveUpdateManager(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,HasManagerItselfAccess]

    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    


   
#Registor Employee  by manager
class EmployeeRegistration(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]     
    permission_classes = [IsAuthenticated]   
    serializer_class = EmployeeSerializer
   
#Employee List under specidfic manager by Manager
class EmployeeList(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    serializer_class = EmployeeSerializer
    def get_queryset(self):
        token = self.request.headers.get('Authorization')
        manager_id = AccessToken(token.split()[1]).payload['user_id']
        emps = Employee.objects.filter(manager_id =manager_id).all()

        return emps

#Employee Retrieve, Update and Destroy By Manager(if emp is under that manager)
class EmployeeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):   
   
    permission_classes = [HasManagerAccessOrNot]

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    

#Log in Employee : Custom Authentication
class EmployeeLogin(generics.CreateAPIView):
    
    authentication_classes = [IsEmployeeOrNot]
    permission_classes = [AllowAny] 
    
    def post(self, request):
        employee = request.user
        
        refresh = RefreshToken.for_user(employee)
        return Response({
            "refresh": str(refresh),
            "access_token": str(refresh.access_token),
        })
#Employee Retrive and Update by employee 
class EmployeeRetrieveUpdate(generics.RetrieveUpdateAPIView):
   
    permission_classes = [IsAuthenticated, IsValidEmployeeOrNot]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    
    
    
