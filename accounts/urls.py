from django.urls import path
from .views import (
    SignUpView,
    TutorUpdateAvailabilityView,
    HomePageView,
    TutorDetailView,
)

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path(
        "update_availability/",
        TutorUpdateAvailabilityView.as_view(),
        name="update_availability",
    ),
    path("", HomePageView.as_view(), name="home"),
    path("tutor/<int:pk>/", TutorDetailView.as_view(), name="tutor_detail"),
]
