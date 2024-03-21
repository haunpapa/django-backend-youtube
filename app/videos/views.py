from django.shortcuts import render
from rest_framework.views import APIView
from .models import Video
from .serializers import VideoListSerializer, VideoDetailSerializer
from rest_framework.response import Response
from rest_framework import status


# Video와 관련된 REST API
# 1. VideoList
# api/v1/video/
#[GET] : 전체 비디오 목록을 가져오는 API
#[POST] : 새로운 비디오를 생성하는 API
#[PUT] : X
#[DELETE] : X

class VideoList(APIView):
    def get(self, request):
        videos = Video.objects.all()
        # 직렬화 (Object -> JSON) - Serializer

        serializer = VideoListSerializer(videos, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user_data = request.data # JSON -> Python Object (역직렬화)
        serializer = VideoListSerializer(data = user_data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 2. VideoDetail
# api/v1/video/<video_id>/
#[GET] : 특정 비디오의 상세 정보를 가져오는 API <상세페이지>
#[POST] : X
#[PUT] : 특정 비디오의 정보를 수정하는 API
#[DELETE] : 특정 비디오를 삭제하는 API
from rest_framework.exceptions import NotFound

class VideoDetail(APIView):
    def get(self, request, pk):
        try :
            video_obj = Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise NotFound('해당 비디오가 존재하지 않습니다.')
        
        serailizer = VideoDetailSerializer(video_obj) # Object -> JSON

        return Response(serailizer.data, status=status.HTTP_200_OK)


    def put(self, request, pk):
        video_obj = Video.objects.get(pk=pk) # db에서 해당 비디오를 가져온다.
        user_data = request.data # 유저가 보낸 데이터

        serializer = VideoDetailSerializer(video_obj, data=user_data)
        serializer.is_valid(raise_exception=True)
        serializer.save() # is_valid() -> save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        video_obj = Video.objects.get(pk=pk)
        video_obj.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)