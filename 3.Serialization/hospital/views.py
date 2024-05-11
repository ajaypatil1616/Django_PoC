from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Doctor, Patient
from .serializers import DoctorSerializer, PatientSerializer

@api_view(['GET', 'POST'])
def doctor_list(request):
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DoctorSerializer(data=request.POST)
        if serializer.is_valid(): #is_valid:validate data during deserialization before writing it to a database
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def patient_list(request):
    if request.method == 'GET':
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PatientSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
