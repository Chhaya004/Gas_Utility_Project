from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.utils.timezone import now

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .forms import ServiceRequestForm

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('submit_request')  # Redirect to submit page
    else:
        form = AuthenticationForm()
    return render(request, 'service_requests/login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

# Protect the Service Request Submission Page
@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to success page
    else:
        form = ServiceRequestForm()
    
    return render(request, 'service_requests/submit_request.html', {'form': form})


def home(request):
    return render(request, 'service_requests/home.html')  # Create home.html later

def submit_request(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("track_request")  # Redirect after successful submission
    else:
        form = ServiceRequestForm()
    
    return render(request, "service_requests/submit_request.html", {"form": form})

def track_request(request):
    requests = ServiceRequest.objects.order_by('-created_at')
    return render(request, "service_requests/track_request.html", {"requests": requests})

def resolve_request(request, request_id):
    """ Marks a service request as resolved """
    service_request = ServiceRequest.objects.get(id=request_id)
    service_request.status = 'resolved'
    service_request.resolved_at = now()
    service_request.save()
    return redirect("track_request")
