from django.shortcuts import render

from django.http import HttpResponse #trail #mahesh

# Create your views here.

#umamaheswar
def user_login(request):
    return render(request, 'login.html', )

#umamaheswar
def user_register(request):
    # Handle the registration logic here
    # You can use Django forms or process the form data manually
    return render(request, 'registration.html')