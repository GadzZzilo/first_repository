from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


# class HomeViewTestCase(TestCase):
#     fixtures = ['developers.json', 'services.json']
#
#     def test_view(self):
#         path = reverse('home')
#         response = self.client.get(path)
#
#         self.assertEqual(response.status_code, HTTPStatus.OK)
#         self.assertEqual(response.context_data['title'], 'Главная')
#         self.assertTemplateUsed(response, "home.html")