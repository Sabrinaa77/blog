from django.forms import ModelForm
from .models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            "name",
            "e-mail",
        ]

        labels = {
            "name": "姓名",
            "e-mail": "電子信箱",
        }
