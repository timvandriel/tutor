from django.urls import path
from .views import SignUpView, TutorUpdateAvailabilityView, HomePageView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path(
        "update_availability/",
        TutorUpdateAvailabilityView.as_view(),
        name="update_availability",
    ),
    path("", HomePageView.as_view(), name="home"),
]
