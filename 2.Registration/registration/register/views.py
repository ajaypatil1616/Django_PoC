from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from .models import RegistrationData

# Create your views here.
def register(request):
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            patient = RegistrationData.objects.create(
            first_name = data['first_name'],
            last_name = data['last_name'],
            age = data['age'],
            email = data['email'],
            password = data['password'],
            confirm_password = data['confirm_password'],
            number = data['number'],
            gender = data['gender'],
            dob = data['dob']
            )
                       
            return render(request, 'registration.html', {'data':data, 'form':form,})
        return render(request, 'registration.html',{'form':form})
    else:
        form = RegistrationForm()       

        return render(request, 'registration.html',{'form':form})

