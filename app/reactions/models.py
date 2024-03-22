from django.db import models
from common.models import CommonModel
from users.models import User
from videos.models import Video
# USER : FK
# VIDEO : FK
# reation_type : like, dislike, cancel

class Reaction(CommonModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    video = models.ForeignKey('videos.Video', on_delete=models.CASCADE)

    LIKE = 1
    DISLIKE = -1
    NO_REACTION = 0


    REACTION_CHOICES = (
        ( 1, 'Like'),
        ( -1 , 'Dislike'),
        ( 0 , 'No Reaction'),
    )



    reaction = models.IntegerField(choices=REACTION_CHOICES, default=NO_REACTION)

    @staticmethod # ORM depth2 모델.objects.get, filther().aggregate() # SQL JOIN query
    def get_video_reaction(video):
        from django.db.models import Count, Q
        reactions = Reaction.objects.filter(video=video).aggregate(
            like_count=Count('pk', filter=Q(reaction=Reaction.LIKE)),
            dislike_count=Count('pk', filter=Q(reaction=Reaction.DISLIKE)),
        )

        return reactions
    


