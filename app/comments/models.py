from django.db import models
from common.models import CommonModel
from users.models import User
from videos.models import Video

class Comment(CommonModel):
    content = models.TextField()
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)

    # User : Comment => 1 : N
    # Comment : User => N : 1


    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Video : Comment => 1 : N
    # Comment : Video => N : 1

    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    # 대댓글 
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')