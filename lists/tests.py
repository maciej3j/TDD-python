from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.template.loader import render_to_string

# Create your tests here.
class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")
