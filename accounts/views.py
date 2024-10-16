from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView
from .forms import CustomUserCreationForm, UpdateAvailabilityForm
from .models import Tutor


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class TutorUpdateAvailabilityView(UpdateView):
    model = Tutor
    form_class = UpdateAvailabilityForm
    template_name = "registration/update_availability.html"
    success_url = reverse_lazy("home")

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        availability = {}
        for day in form.cleaned_data["available_days"]:
            hours_field = f"{day}_hours"
            availability[day] = form.cleaned_data[hours_field]
        self.request.user.availability = availability
        self.request.user.save()
        return super().form_valid(form)


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tutors"] = Tutor.objects.all()
        return context
