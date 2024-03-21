from rest_framework import serializers
from .models import Subscription

class SubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

    # 내가 나를 구독할 수 있나? 없다 ! 
    def validate(self, data): #data => DataType(dict)
        if data['subscriber'] == data['subscribed_to']:
            raise serializers.ValidationError('You can\'t subcribe to yourself.')
        
        return data