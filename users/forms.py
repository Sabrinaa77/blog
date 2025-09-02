from django.forms import ModelForm
from .models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            "name",
            "email",
        ]

        labels = {
            "name": "姓名",
            "email": "電子信箱",
        }
