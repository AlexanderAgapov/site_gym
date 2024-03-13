from django.contrib.auth.models import User
from rest_framework import serializers
from users.models import User

class GymSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = User
        fields = ('username', 'email', 'user',)
