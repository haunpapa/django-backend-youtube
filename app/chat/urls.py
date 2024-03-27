from django.urls import path

from .views import ChatRoomList, ChatMessageList, chat_html

urlpatterns = [
    path('room/', ChatRoomList.as_view(), name='room-list'),
    path('<int:room_id>/messages', ChatMessageList.as_view(), name='chat-message'),
    path('chatting',chat_html, name='chatting')
]