from django.db import models
from common.models import CommonModel
class ChatRoom(CommonModel):
    name = models.CharField(max_length=100)


class ChatMessage(CommonModel):
    sender = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    message = models.TextField()
    room = models.ForeignKey('ChatRoom', on_delete=models.CASCADE)
