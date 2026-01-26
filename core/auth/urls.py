from django.urls import path
from .views import signup,google_callback

urlpatterns = [
    path("signup/", signup),
    path("google/callback/", google_callback),
    # path("linkedin/callback/", linkedin_callback),
]
