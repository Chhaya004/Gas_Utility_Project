from django.urls import path, include
from .views import submit_request, track_request, resolve_request

urlpatterns = [
    path("submit/", submit_request, name="submit_request"),
    path("track/", track_request, name="track_request"),
    path("resolve/<int:request_id>/", resolve_request, name="resolve_request"),
    
    
    path("accounts/", include("django.contrib.auth.urls")),
]
