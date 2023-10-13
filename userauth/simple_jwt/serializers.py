from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from userauth.models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: User):
        token = super().get_token(user)

        token['groups'] = list(user.permission_groups.values_list('code', flat=True))
        
        return token