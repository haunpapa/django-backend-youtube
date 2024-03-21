from django.db import models
from common.models import CommonModel
from users.models import User

# User : FK -> Subsriber (내가 구독한사람)
# User : FK -> Subscribed_to (나를 구독한사람)

# User:Subscriber = User(Subscriber) => subscriber

class Subscription(CommonModel):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    subscribed_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribers')