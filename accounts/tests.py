from django.test import TestCase
from .models import Tutor


class TutorModelTests(TestCase):

    def test_create_tutor(self):
        tutor = Tutor.objects.create_user(
            username="testtutor",
            password="password123",
            email="testtutor@example.com",
            first_name="Test",
            last_name="Tutor",
            subjects="Math, Science",
        )
        self.assertEqual(tutor.username, "testtutor")
        self.assertEqual(tutor.email, "testtutor@example.com")
        self.assertEqual(tutor.first_name, "Test")
        self.assertEqual(tutor.last_name, "Tutor")
        self.assertEqual(tutor.subjects, "Math, Science")
        self.assertEqual(tutor.availability, {})

    def test_default_availability(self):
        tutor = Tutor.objects.create_user(
            username="testtutor2",
            password="password123",
            email="testtutor2@example.com",
            first_name="Test2",
            last_name="Tutor2",
            subjects="English, History",
        )
        self.assertEqual(tutor.availability, {})

    def test_update_availability(self):
        tutor = Tutor.objects.create_user(
            username="testtutor3",
            password="password123",
            email="testtutor3@example.com",
            first_name="Test3",
            last_name="Tutor3",
            subjects="Physics, Chemistry",
        )
        tutor.availability = {
            "Monday": ["9:00-11:00", "14:00-16:00"],
            "Wednesday": ["10:00-12:00"],
        }
        tutor.save()
        updated_tutor = Tutor.objects.get(username="testtutor3")
        self.assertEqual(
            updated_tutor.availability,
            {"Monday": ["9:00-11:00", "14:00-16:00"], "Wednesday": ["10:00-12:00"]},
        )

    def test_create_superuser(self):
        superuser = Tutor.objects.create_superuser(
            username="superuser",
            password="superpassword123",
            email="superuser@example.com",
            first_name="Super",
            last_name="User",
            subjects="Admin",
        )
        self.assertEqual(superuser.username, "superuser")
        self.assertEqual(superuser.email, "superuser@example.com")
        self.assertEqual(superuser.first_name, "Super")
        self.assertEqual(superuser.last_name, "User")
        self.assertEqual(superuser.subjects, "Admin")
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)
        self.assertEqual(superuser.availability, {})
