from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import *

# Create your tests here.
class PostModeltestCase (TestCase):
    def setUp(self):
            some_random_user=User.objects.create(username='pepsi1111111'),

    def test_post_item(self):
        obj = Post.objects.create(
        author=User.objects.first(),
        content='Some random content'
        )
        self.assertTrue(obj.content == 'Some random content')
        self.assertTrue(obj.id == 1)
        absolute_url = reverse("detail", kwargs={"post_id": 1})
        self.assertEqual(obj.get_absolute_url(), absolute_url)

