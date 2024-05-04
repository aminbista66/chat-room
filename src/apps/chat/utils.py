from rest_framework.authtoken.models import Token

def get_user(token):
    try:
        return Token.objects.get(key=token).user
    except Token.DoesNotExist:
        return None
