from django.test import TestCase
from rest_framework.test import APITestCase
from users.models import User
from rest_framework.reverse import reverse
from rest_framework import status
from .models import Subscription
from rest_framework.response import Response


class SubscriptionTestCase(APITestCase):
    # 테스트 코드 실행 시 가장 먼저 실행되는 함수
    # 데이터 생성
    # 2명의 유저 데이터 생성

    def setUp(self):
        self.user1 = User.objects.create_user(email = 'oz12@oz.com', password = '1234')
        self.user2 = User.objects.create_user(email = 'oz23@oz.com', password = '1234')

        self.client.login(email = 'oz12@oz.com', password = '1234')

    # 구독 버튼 테스트 
    def test_sub_list_post(self):
        url = reverse('sub-list')

        data ={
            'subscriber' : self.user1.pk,
            'subscribed_to' : self.user2.pk
        }

        res = self.client.post(url, data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
       
        self.assertEqual(Subscription.objects.get().subscribed_to, self.user2)
        self.assertEqual(Subscription.objects.count(), 1)



    # 특정 유저의 구독자 리스트 
    def test_sub_detail_get(self):
        # 구독 생성
        subscription = Subscription.objects.create(subscriber=self.user1, subscribed_to=self.user2)

        pk = subscription.pk

        url = reverse('sub-detail', kwargs={'pk': pk})

        res = self.client.get(url)

        # HTTP 200 OK 응답 확인
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        # 응답 데이터 검증
        data = res.json()

        self.assertEqual(data['subscriber'], self.user1.pk)
        self.assertEqual(data['subscribed_to'], self.user2.pk)

    def test_sub_detail_delete(self):
        # 구독 생성
        subscription = Subscription.objects.create(subscriber=self.user1, subscribed_to=self.user2)

        pk = subscription.pk

        url = reverse('sub-detail', kwargs={'pk': pk})

        self.client.force_authenticate(user=self.user1)  # 구독자로 인증
        res = self.client.delete(url)  # delete 요청

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Subscription.objects.filter(pk=pk).exists())  # 구독이 삭제되었는지 확인