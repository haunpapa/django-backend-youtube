from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ChatRoomSerializer
from .models import ChatRoom, ChatMessage
from rest_framework import status


# ChatRoom
## ChatRoom List
### [Get] : 전체 채팅방 조회
### [Post] : 채팅방 생성

class ChatRoomList(APIView):
    def get(self, request):
        chatrooms = ChatRoom.objects.all()
        serializer = ChatRoomSerializer(chatrooms, many=True)

        return Response(serializer.data)

    def post(self, request):
        user_data = request
        serializer = ChatRoomSerializer(data=user_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)             



## ChatRoom Detail
### [PUT] : 채팅방 관련 수정
### [DELETE] : 해당 채팅방 삭제
    


# ChatMessage
## ChatMessage List
### [Get] : 전체 메세지 조회
### [Post] : 메세지 생성
    
from django.shortcuts import get_object_or_404
from .serializers import ChatMessageSerializer
from django.shortcuts import render

def chat_html(request):
    return render(request, 'index.html') # html 파일을 렌더링
    
class ChatMessageList(APIView):
    def get(self,request, room_id):
        chatroom = get_object_or_404(ChatRoom, id=room_id)
        messages = ChatMessage.objects.filter(room=chatroom)

        serializer = ChatMessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request, room_id):
        chatroom = get_object_or_404(ChatRoom, id=room_id)
        user_data = request.data
        serializer = ChatMessageSerializer(data=user_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)