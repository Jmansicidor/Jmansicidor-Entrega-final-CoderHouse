from django.forms import ModelForm
from usuarios.models import User


class UserForms(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {

        }