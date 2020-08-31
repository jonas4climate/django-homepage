from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from .views import post_list

class HomePageTest(TestCase):
      
   def test_home_page_returns_correct_html(self):
      response = self.client.get('/')
      self.assertTemplateUsed(response, 'blog/post_list.html')