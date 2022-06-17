from django.forms import ModelForm
from usuarios.models import UserInfo


class UserForms(ModelForm):
    class Meta:
        model = UserInfo
        fields = '__all__'
        widgets = {

        }