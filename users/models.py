from django.contrib.auth.models import User

class User(User):
    username = User.username