from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Subscription
from .serializers import SubSerializer
from rest_framework.exceptions import NotFound
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
# 구독 관련 REST API
# api/v1/subscriptions/vz S\\
# [POST] : 구독하기

# SubscriptionDetail5
# api/v1/subscriptions/{user_id}/
# [GET] : 특정 유저의 구독자 목록을 가져오는 API
# [DELETE] : 구독 취소하기

class SubscriptionList(APIView):
    def post(self, request):
        user_data = request.data # JSON -> Python Object (역직렬화)
        serializer = SubSerializer(data = user_data)
        serializer.is_valid(raise_exception=True)
        serializer.save(subscriber=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED) 

    def delete(self, request):
        pass

class SubscriptionDetail(APIView):
    def get(self, request, pk):
        try :
            subs_obj = Subscription.objects.get(pk=pk)
            serializer = SubSerializer(subs_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Subscription.DoesNotExist:
            raise NotFound('해당 구독이 존재하지 않습니다.')
        
    def delete(self, request, pk):
        # 삭제할 구독의 ID를 request.data에서 가져옵니다.
        try:
            subscription = get_object_or_404(Subscription, pk=pk)
        except Subscription.DoesNotExist:
            return Response({'error': '해당 구독이 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)

        subscription.delete()
        return Response({'message': '구독이 성공적으로 취소되었습니다.'}, status=status.HTTP_204_NO_CONTENT)
        
    