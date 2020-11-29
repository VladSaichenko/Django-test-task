from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from apps.memories.models import Memory


class MemoryAPITest(APITestCase):
    def setUp(self):
        self.test_user1 = User.objects.create(username='Guido', password='python123', email='py@mail.com')
        self.test_user2 = User.objects.create(username='Linus', password='linux123', email='linux@mail.com')

        Memory.objects.create(user=self.test_user1, title='Концерт 12.02.2009', text='Было классно!', longitude=23.12, latitude=32.11)

        self.count_before = Memory.objects.count()

        self.memory_correct_instance = {
            'title': 'Концерт 12.02.2009',
            'text': 'Было классно!',
            'longitude': 23.12,
            'latitude': 32.11,
        }
        self.memory_incorrect_instance = {
            'title': 'Концерт 12.02.2009',
            'text': 'Было классно!',
            'longitude': 'Где-то там',
            'latitude': 'Очень далеко',
        }

    def test_create_action_correct_instance(self):
        """
        Test that user can create memory.
        """
        client = APIClient()
        client.force_authenticate(user=self.test_user1)
        url = reverse('memory-list')

        response = client.post(url, self.memory_correct_instance, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Memory.objects.count(), self.count_before + 1)

        self.assertTrue('id' in response.data)
        self.assertTrue('user' in response.data)
        self.assertTrue('title' in response.data)
        self.assertTrue('text' in response.data)
        self.assertTrue('longitude' in response.data)
        self.assertTrue('latitude' in response.data)

    def test_create_action_incorrect_instance(self):
        """
        Test that user can not create memory with invalid data.
        """
        client = APIClient()
        client.force_authenticate(user=self.test_user1)
        url = reverse('memory-list')

        response = client.post(url, self.memory_incorrect_instance, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Memory.objects.count(), self.count_before)

    def test_update_action(self):
        """
        Test that user can update its memory.
        """
        client = APIClient()
        client.force_authenticate(user=self.test_user1)
        obj = Memory.objects.filter(user=self.test_user1).first()

        url = reverse('memory-detail', args=(obj.id, ))
        response = client.put(url, self.memory_correct_instance, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_action_by_not_owner(self):
        """
        Test that user can not update others memories.
        """
        client = APIClient()
        client.force_authenticate(user=self.test_user2)
        obj = Memory.objects.filter(user=self.test_user1).first()

        url = reverse('memory-detail', args=(obj.id, ))
        response = client.put(url, self.memory_correct_instance, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_action_by_not_owner(self):
        """
        Test that user can not delete others memories.
        """
        client = APIClient()
        client.force_authenticate(user=self.test_user2)
        obj = Memory.objects.filter(user=self.test_user1).first()

        url = reverse('memory-detail', args=(obj.id, ))
        response = client.delete(url, self.memory_correct_instance, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_action(self):
        """
        Test that user can delete its memory.
        """
        client = APIClient()
        client.force_authenticate(user=self.test_user1)
        obj = Memory.objects.filter(user=self.test_user1).first()

        url = reverse('memory-detail', args=(obj.id, ))
        response = client.delete(url, self.memory_correct_instance, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_memory_list_action(self):
        """
        Test that `list` action for Memory returns list of objects with all fields.
        """
        client = APIClient()
        client.force_authenticate(user=self.test_user1)
        url = reverse('memory-list')
        response = client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), self.count_before)

    def test_memory_retrieve_action(self):
        """
        Test that GET by id returns correct data.
        """
        client = APIClient()
        client.force_authenticate(user=self.test_user1)
        obj = Memory.objects.first()

        url = reverse('memory-detail', args=(obj.id, ))
        response = client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], obj.id)
        self.assertEqual(response.data['user'], obj.user.id)
        self.assertEqual(response.data['title'], obj.title)
        self.assertEqual(response.data['text'], obj.text)
        self.assertEqual(response.data['longitude'], str(obj.longitude))
        self.assertEqual(response.data['latitude'], str(obj.latitude))
