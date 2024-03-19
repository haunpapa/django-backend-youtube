from django.test import TestCase
from rest_framework.test import APITestCase
from users.models import User
from .models import Video
from django.urls import reverse
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile

# Video와 관련된 REST API 테스트

class VideoAPITestCase(APITestCase):
    def setup(self):
        self.user = User.objects.create_user(
            email = 'oz@oz.com',
            password = '1234'
        )

        self.client.login(email ='oz@oz.com', password = '1234')

        self.Video.objects.create(
            title = 'test video',
            link = 'https://www.test.com/',
            user = self.user
        )

    # 127.0.0.1:8000/api/v1/video [GET]
    def test_video_list_get(self):
        # url = 'http://127.0.0.1:8000/api/v1/video/'
        url = reverse('video-list')
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.headers['Cotent-Type'], 'application/json')
        self.assertTrue(len(res.data) > 0)

        #title이 있는지 확인
        for video in res.data:
            self.assertIn('title', video)


    def test_video_list_post(self):
        url = reverse('video-list')

        data ={
            'title' : 'test video2',
            'link' : 'https://www.test.com/',
            'category' : 'test',
            'thumbnail' : 'https://www.test.com/',
            'video_file' : SimpleUploadedFile('test.mp4', b'test', content_type='video/mp4'),
            'user' : self.user.pk
        }

        res = self.client.post(url, data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['title'], 'test video2')

    def test_video_detail_get(self):
        pass    

    def test_video_detail_put(self):
        pass
    
    def test_video_detail_delete(self):
        pass
