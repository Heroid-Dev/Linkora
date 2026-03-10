from rest_framework import serializers
from connections.models import Connection
from accounts.models import Profile

class ConnectionSerializer(serializers.ModelSerializer):
    
    follower=serializers.StringRelatedField(read_only=True)
    following=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Connection
        fields=['id','follower','following','established_date']
        
        
        

class ProfileListSerializer(serializers.ModelSerializer):
    is_following=serializers.SerializerMethodField()
    class Meta:
        model=Profile
        fields=['id','username','user_type','bio','is_following']

    def get_is_following(self,obj):
        user=self.context.get('request').user
        if not user.is_authenticated:
            return False
        return Connection.objects.filter(follower=user.profile,following=obj).exists()
        