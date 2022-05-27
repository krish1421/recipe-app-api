"""
Tests for the django admin modification
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):
    """ test for django admin"""

    def setUp(self):
        """create user and client"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='krishna@gmail.com',
            password='12345'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@gmail.com',
            password='testpass123',
            name='Test User'
        )

    def test_users_list(self):
        """test that Users are list"""
        url = reverse('admin:core_user_changelist')
        res  = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        """test the edit_user_page works"""
        url = reverse('admin:core_user_change', args=[self.admin_user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """test the create_user_page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

        
