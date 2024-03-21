from django.test import TestCase
from rest_framework.test import APITestCase
from users.models import User
from .models import Video
from django.urls import reverse
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
import pdb #Python DeBugger

# Video와 관련된 REST API 테스트

class VideoAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email = 'oz@oz.com',
            password = '1234'
        )

        self.client.login(email ='oz@oz.com', password = '1234')

        self.video =Video.objects.create(
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
        self.assertEqual(res.headers['Content-Type'], 'application/json')
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
            'video_file' : SimpleUploadedFile('test.mp4', b'file_content', content_type='video/mp4'),
            'user' : self.user.pk
        }

        # pdb.set_trace()

        res = self.client.post(url, data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['title'], 'test video2')

    # 특정 비디오 조회
    def test_video_detail_get(self):
        url = reverse('video-detail', kwargs={'pk':self.video.pk})
        # url: api/v1/video/1

        res = self.client.get(url) # [GET] api/v1/video/1

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    # 특정 비디오 업데이트하는 코드
    def test_video_detail_put(self):       
        url = reverse('video-detail', kwargs={'pk':self.video.pk})

        data = {
            'title':'updated video',
            'link':'http://test.com',
            'category':'test category',
            'thumbnail':'http://test.com',
            'video_file': SimpleUploadedFile('file.mp4', b'file_content', 'video/mp4'),
            'user': self.user.pk
        }
        
        res = self.client.put(url, data) # 서버에 요청 -> res

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['title'], 'updated video')      

    # 특정 비디오 삭제
    def test_video_detail_delete(self):
        url = reverse('video-detail', kwargs={'pk':self.video.pk})
        res = self.client.delete(url) # [DELETE] api/v1/video/{pk} -> REST API
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

        res = self.client.get(url) # [GET] api/v1/video/{pk}
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    # 테스트 코드 실행
    # docker-compose run --rm app sh -c 'python manage.py test videos'
